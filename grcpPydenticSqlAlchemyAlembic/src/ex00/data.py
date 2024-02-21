import air_craft_pb2
from faker import Faker
import random


## random officers form START to END
START = 1
END = 5

## Task Constants
ALIGNMENT = ["Ally", "Enemy"]
CLASS_TYPE = ["Corvette", "Frigate", "Cruiser", "Destroyer", "Carrier", "Dreadnought"]
ARMED = [True, False]
RANK = ["Commander", "Teacher", "Student", "Allien", "Human"]
fake = Faker()


DATA_BOUNDS = {
    "Corvette": {
        "l": [80, 250],
        "s": [4, 10],
        "ar": True,
        "al": True,
    },
    "Frigate": {
        "l": [300, 600],
        "s": [10, 15],
        "ar": True,
        "al": False,
    },
    "Cruiser": {
        "l": [500, 1000],
        "s": [15, 30],
        "ar": True,
        "al": True,
    },
    "Destroyer": {
        "l": [800, 2000],
        "s": [50, 80],
        "ar": True,
        "al": False,
    },
    "Carrier": {
        "l": [1000, 4000],
        "s": [120, 250],
        "ar": False,
        "al": True,
    },
    "Dreadnought": {
        "l": [5000, 20000],
        "s": [300, 500],
        "ar": True,
        "al": True,
    },
}
RANDOM_ = {
    "l": [80, 200000],
    "s": [4, 1000],
    "ar": True,
    "al": True,
}


class Data:
    fake = Faker()

    def generate_data(self):
        data = air_craft_pb2.ResponceAircraft()
        self._class = random.choice(CLASS_TYPE)
        flag = random.choice([True, False, False, False])

        data._class = self._class
        data.length = self.get_length(flag)
        data.crew_size = self.get_size(flag)
        data.armed = self.get_armed(flag)
        data.aligment = self.get_alignment(flag)
        data.name = fake.name().split(" ")[0]
        for _ in range(random.randint(START, END)):
            item = data.officers.add()
            item.first_name = fake.name().split(" ")[0]
            item.last_name = fake.name().split(" ")[1]
            item.rank = random.choice(RANK)
        return data

    def get_length(self, flag):
        if flag:
            l = DATA_BOUNDS[self._class]["l"]
        else:
            l = RANDOM_["l"]
        return random.randint(l[0], l[1])

    def get_size(self, flag):
        if flag:
            s = DATA_BOUNDS[self._class]["s"]
        else:
            s = RANDOM_["s"]
        return random.randint(s[0], s[1])

    def get_armed(self, flag):
        if flag:
            return DATA_BOUNDS[self._class]["ar"]
        else:
            return random.choice(ARMED)

    def get_alignment(self, flag):
        if not flag:
            return random.choice(ALIGNMENT)
        al = DATA_BOUNDS[self._class]["al"]
        if al:
            return "Enemy"
        else:
            return "Ally"


if __name__ == "__main__":
    data = Data()
    print(data.generate_data())
