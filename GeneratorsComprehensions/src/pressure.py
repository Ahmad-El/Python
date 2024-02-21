import time
import random

TIME_SLEEP = 0.3


def emit_gel(user_step: int):
    value = 50
    while True:
        start = min(0, user_step)
        end = max(0, user_step)
        random_step = random.randint(start, end)
        i = yield value
        if i is not None:
            random_step *= i
            user_step *= i
        value += random_step


def valve(generator):
    flag = True
    while flag:
        time.sleep(TIME_SLEEP)
        value = next(generator)
        if value >= 90 or value <= 10:
            if value > 100:
                print("Error")
            else:
                print("Emergency break")
            generator.close()
            flag = False
        elif value < 20 or value > 80:
            if (value < 20):
                print("Pressure below 20")
            else:
                print("Pressure above 80")
            generator.send(-1)
        else:
            print(value)


if __name__ == "__main__":
    valve(emit_gel(20))
