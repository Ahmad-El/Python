import grpc
import air_craft_pb2
import air_craft_pb2_grpc
import json
import sys


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
            print(
                json.dumps(
                    {
                        "alignment": air_craft_pb2.AlignmentType.Name(item.aligment),
                        "name": item.name,
                        "class": air_craft_pb2.ClassEnum.Name(item._class),
                        "length": item.length,
                        "crew_size": item.crew_size,
                        "armed": item.armed,
                        "officers": [
                            {
                                "fist_name": officer.first_name,
                                "last_name": officer.last_name,
                                "rank": officer.rank,
                            }
                            for officer in item.officers
                        ],
                    },
                    indent=4,
                )
            )


if __name__ == "__main__":
    coordinates = parse_coordinates()
    if len(coordinates) == 6:
        run(coordinates)
    else:
        print("Input Error")
