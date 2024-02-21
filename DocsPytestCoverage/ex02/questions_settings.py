import json
import random
import time
import os

OPTIONS = ["a", "b", "c", "d", "e"]
DATA_FILE = "ex01/data.json"


class Questions:
    """
    A class used to generate questions and manipulate with them
    ...

    Attributes
    ----------
    total_points : int
        a point earned after answering questions
    current_question : int
        current question id
    answer : str
        last questions answer
    data : list
        list of questions by default 10

    Methods
    -------
    next()
        move to next question
    reset(n)
        resets question data and attributes
    print_question(question)
        prints current question
    get_ten_random_questions(n, file_name=DATA_FILE)
        restores questions to data
    """

    def __init__(self, number_of_questions=10) -> None:
        """
        Parameters
        ----------
        number_of_questions : int
            number of question to prompt by default is 10
        """
        self.total_points = 0
        self.current_question = 0
        self.get_ten_random_questions(number_of_questions)

    def next(self):
        """Moves to next question

        Returns:
        ----------
        bool: question not ended
        """
        self.answer = self.print_question(self.data[self.current_question])
        self.current_question += 1
        return self.current_question < len(self.data)

    def reset(self, total_number_questions):
        """Resets question data and its attributes

        If the argument `total_number_questions` isn't passed in,
        the default question count is used.

        Parameters
        ----------
        total_number_questions : int, optional
            The sound the animal makes (default is None)
        """
        self.current_question = 0
        self.total_points = 0
        self.get_ten_random_questions(total_number_questions)

    def print_question(self, question):
        """Prints the question and prompts for input

        If input is invalid it recursively prompts till valid input

        Parameters
        ----------
        question : dict, required
            The sound the animal makes (default is None)


        Returns:
        ---------
        str: your input(answer to current question)
        """
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
        """Generates n question and appends to question data

        If file_name isn't passed in, the default file data used.


        Parameters
        ----------
        file_name : str, optional
            The data file of questions
        n: int required

        Warning
        ------
        Data file not found
            If file path not found
        """
        if not os.path.exists(file_name):
            print("data file not found")
        else:
            with open(file_name, "r") as file:
                json_data = json.load(file)
            self.data = [random.choice(json_data) for _ in range(n)]
