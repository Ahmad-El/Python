import random


RESPIRATORY = [12, 20]
HEART_RATE = [60, 100]
MAX_BLUSHING_LEVEL = 6
PUPILLARY = [2, 8]


class Retirement:
    def cal_respiration(self):
        return random.randint(RESPIRATORY[0], RESPIRATORY[1])

    def cal_heart_rate(self):
        return random.randint(HEART_RATE[0], HEART_RATE[1])

    def cal_blushing_level(self):
        return random.randint(1, MAX_BLUSHING_LEVEL)

    def cal_pupillary(self):
        return random.randint(PUPILLARY[0], PUPILLARY[1])

    def calculate(self, total_time, points):
        self.resp = self.cal_respiration()
        self.heart = self.cal_heart_rate()
        self.bulush = self.cal_blushing_level()
        self.pupil = self.cal_pupillary()
        print(
            f"The result of test - total time: {total_time}, total earned points for questions: {points}"
        )
        self.print_the_result()

    def print_the_result(self):
        print()
        print("============================  RESULT  ==============================")
        print(
            f"Your respiration: {self.resp} (measured in BPM, normally around 12-16 breaths per minute"
        )
        print(
            f"Your Heart rate: {self.heart} (normally around 60 to 100 beats per minute)"
        )
        print(f"Your blushing level: {self.bulush} (categorical, 6 possible levels)")
        print(f"Your pupillary dilation: {self.pupil}")
        print("Congratulations you are human!")
        print("====================================================================")
        print()
