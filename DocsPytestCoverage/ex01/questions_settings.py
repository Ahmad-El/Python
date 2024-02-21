import json
import random
import time
import os

OPTIONS = ["a", "b", "c", "d", "e"]
DATA_FILE = "ex01/data.json"


class Questions:
    def __init__(self, number_of_questions=10) -> None:
        self.total_points = 0
        self.current_question = 0
        self.get_ten_random_questions(number_of_questions)

    def next(self):
        self.answer = self.print_question(self.data[self.current_question])
        self.current_question += 1
        return self.current_question < len(self.data)

    def reset(self, total_number_questions):
        self.current_question = 0
        self.total_points = 0
        self.get_ten_random_questions(total_number_questions)

    def print_question(self, question):
        print(question["question"])
        print(f"a) {question['a']}")
        print(f"b) {question['b']}")
        print(f"c) {question['c']}")
        print(f"d) {question['d']}")
        print(f"e) {question['e']}")

        answer = str(input("Your answer: ")).strip().lower()
        if answer not in OPTIONS:
            print("Invalid Input")
            return self.print_question(question)
        self.total_points += question["points"][ord(answer) - 97]
        return answer

    def get_ten_random_questions(self, n, file_name=DATA_FILE):
        if not os.path.exists(file_name):
            print("data file not found")
        else:
            with open(file_name, "r") as file:
                json_data = json.load(file)
            self.data = [random.choice(json_data) for _ in range(n)]
