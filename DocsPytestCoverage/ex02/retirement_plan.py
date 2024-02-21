import random


RESPIRATORY = [12, 20]
HEART_RATE = [60, 100]
MAX_BLUSHING_LEVEL = 6
PUPILLARY = [2, 8]


class Retirement:
    """
    A class used to make decision you are human or replicant
    ...

    Attributes
    ----------
    total_points: int
        total points you earned from questions
    total_time:
        total answered time
    flag:
        decision maked with AI True

    Methods
    --------
    cal_respiration()
        calculates and returns your respiration measured in BPM
    cal_heart_rate()
        calculates and returns your heart rate
    cal_blushing_level()
        calculates and returns your blushing level
    cal_pupillary()
        calculates average size of your pupillary size
    cal_calculate()
        makes decision are you human or replicant
    print_the_result()
        prints results of your after calculating
    human_or_replicant()
        prints the result human or replicant

    """

    def cal_respiration(self):
        """Calculates Human respiration

        Returns:
        ----------
            int: returns human respiration measured in
        """
        return random.randint(RESPIRATORY[0], RESPIRATORY[1])

    def cal_heart_rate(self):
        """Calculates heart rate

        Returns:
        ----------
            int: returns heart rate for period answered for questions
        """
        return random.randint(HEART_RATE[0], HEART_RATE[1])

    def cal_blushing_level(self):
        """Calculates Blushing level in blood

        Returns:
        ---------
            int: returns blushing level
        """
        return random.randint(1, MAX_BLUSHING_LEVEL)

    def cal_pupillary(self):
        """Calculates average pupil size while answering to questions

        Returns:
        --------
            int: returns pupil size
        """
        return random.randint(PUPILLARY[0], PUPILLARY[1])

    def calculate(self, total_time, points):
        """Calculates all of them and makes decision

        Parameters:
        -----------
            total_time (float): total time for passing all questions
            points (int): total points earned for questions
        """
        self.flag = True
        self.total_time = total_time
        self.points = points

        if total_time < 13 or points <= 65:
            self.flag = False

        self.resp = self.cal_respiration()
        self.heart = self.cal_heart_rate()
        self.bulush = self.cal_blushing_level()
        self.pupil = self.cal_pupillary()
        if self.flag == False:
            self.resp += int(self.resp / 2)
            self.heart -= int(self.heart / 2)

    def print_the_result(self):
        """Prints information for given result"""
        print(
            f"The result of test - total time: {self.total_time}, total earned points for questions: {self.points}"
        )

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
        self.human_or_replicant()
        print("====================================================================")
        print()

    def human_or_replicant(self):
        """Prints decision result you are human or replicant"""
        if self.flag:
            print("Congratulations you are human!")
        else:
            print("You are Replicant")
