from questions_settings import Questions
from retirement_plan import Retirement
import time


def main():
    questions = Questions(10)
    start = time.time()
    while questions.next():
        pass
    end = time.time()

    humanity = Retirement()
    humanity.calculate(end - start, questions.total_points)
    humanity.print_the_result()


if __name__ == "__main__":
    main()
