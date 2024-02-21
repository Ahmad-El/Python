from questions_settings import Questions
from retirement_plan import Retirement


def main():
    questions = Questions(10)
    questions.start()
    humanity = Retirement()
    humanity.calculate(questions.total_time, questions.total_points)


if __name__ == "__main__":
    main()
