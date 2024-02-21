from ..questions_settings import Questions
from ..retirement_plan import Retirement
from io import StringIO
import pytest


class Tester:
    questions = Questions(10)

    def test_count_questions(self):
        assert len(self.questions.data) == 10

    def test_for_file_existens(self, capsys):
        self.questions.get_ten_random_questions(10, "file_not_exist")
        captured = capsys.readouterr()
        assert captured.out == "data file not found\n"

    def get_message(self):
        self.questions.next()
        return self.questions.answer

    def test_get_message(self, monkeypatch):
        user_input = "a"
        monkeypatch.setattr("builtins.input", lambda prompt: user_input)
        message = self.get_message()
        assert message == "a"

    def test_get_message_invalid_input_message(self, monkeypatch):
        user_input = ["invalid input", "kalsdjf", "a"]

        def get_inputs(prompt):
            return user_input.pop(0)

        monkeypatch.setattr("builtins.input", get_inputs)
        captured_output = StringIO()
        monkeypatch.setattr("sys.stdout", captured_output)
        message = self.get_message()
        assert message == "a"

    def test_for_resetting_questions(self):
        self.questions.reset(10)
        assert self.questions.current_question == 0
        assert self.questions.total_points == 0


# if __name__ == "__main__":
#     pytest.main()
