import grpc
import air_craft_pb2
import air_craft_pb2_grpc
import json
import sys
from pydantic import BaseModel, conlist, computed_field, Field
from data import DATA_BOUNDS


class Officer(BaseModel):
    first_name: str
    last_name: str
    rank: str


class ShipModel(BaseModel):
    alignment: str
    name: str
    class_: str = Field(..., alias="class")
    length: float
    crew_size: int
    armed: bool
    officers: conlist(Officer)

    @computed_field
    def is_valid(self) -> bool:
        data = DATA_BOUNDS.get(self.class_)
        if not self.value_is_ok(data["l"][0], data["l"][1], self.length):
            return False
        if not self.value_is_ok(data["s"][0], data["s"][1], self.crew_size):
            return False
        if not self.armed == data["ar"]:
            return False
        if data["al"] == False and self.alignment == "Enemy":
            return False
        return True

    def value_is_ok(self, i: int, f: int, value: float) -> bool:
        return value >= i and value <= f


def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def parse_coordinates():
    args = sys.argv[1:]
    coors = []
    for arg in args:
        arg = arg.strip()

        if is_float(arg):
            coors.append(float(arg))
        else:
            return []
    return coors


def run(coordinates):
    with grpc.insecure_channel("localhost:50052") as channel:
        stub = air_craft_pb2_grpc.ShipsServiceStub(channel)
        for item in stub.GetAircraft(
            air_craft_pb2.RequestSpaceCoor(coordinates=coordinates)
        ):
            data = responce_to_dict(item)
            try:
                if ShipModel(**data).is_valid:
                    print(json.dumps(data, indent=4))
            except:
                pass


def responce_to_dict(item):
    data = {
        "alignment": air_craft_pb2.AlignmentType.Name(item.aligment),
        "name": item.name,
        "class": air_craft_pb2.ClassEnum.Name(item._class),
        "length": item.length,
        "crew_size": item.crew_size,
        "armed": item.armed,
        "officers": [
            {
                "first_name": officer.first_name,
                "last_name": officer.last_name,
                "rank": officer.rank,
            }
            for officer in item.officers
        ],
    }
    return data


def main():
    coordinates = parse_coordinates()
    if len(coordinates) == 6:
        run(coordinates)
    else:
        print("Input Error")


if __name__ == "__main__":
    main()
