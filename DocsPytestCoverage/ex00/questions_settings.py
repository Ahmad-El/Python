import json
import random
import time

OPTIONS = ["a", "b", "c", "d", "e"]
DATA_FILE = "ex00/data.json"


class Questions:
    def __init__(self, number_of_questions) -> None:
        self.total_points = 0
        self.get_ten_random_questions(number_of_questions)

    def start(self):
        start_time = time.time()
        for question in self.data:
            self.print_question(question)
        end_time = time.time()
        self.total_time = end_time - start_time

    def reset(self, total_number_questions):
        self.get_ten_random_questions(total_number_questions)
        self.total_points = 0
        self.total_time = 0

    def print_question(self, question):
        print(question["question"])
        print(f"a) {question['a']}")
        print(f"b) {question['b']}")
        print(f"c) {question['c']}")
        print(f"d) {question['d']}")
        print(f"e) {question['e']}")

        answer = input().strip().lower()
        if answer not in OPTIONS:
            print("Invalid Input")
            return self.print_question(question)
        self.total_points += question["points"][ord(answer) - 97]
        return answer

    def get_ten_random_questions(self, n):
        with open(DATA_FILE, "r") as file:
            json_data = json.load(file)
        self.data = [random.choice(json_data) for _ in range(n)]
