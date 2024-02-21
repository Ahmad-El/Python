# content of test_sample.py
from ..questions_settings import Questions
from ..retirement_plan import Retirement
import pytest
import time

import pytest


class TestReirement:
    questions = Questions(10)
    retirement = Retirement()

    def get_message(self):
        self.questions.next()
        return self.questions.answer

    def check_input(self, monkeypatch):
        user_input = "a"
        monkeypatch.setattr("builtins.input", lambda _: user_input)
        message = self.get_message()
        assert message == "a"

    def test_for_replicant(self, capsys, monkeypatch):
        start = time.time()
        for _ in range(10):
            self.check_input(monkeypatch)
        end = time.time()
        self.retirement.calculate(end - start, self.questions.total_points)

    def test_for_replicant2(self, capsys):
        self.retirement.human_or_replicant()
        captured = capsys.readouterr()
        assert captured.out == "You are Replicant\n"

    def test_for_human(self, capsys):
        self.retirement.calculate(16, 90)
        self.retirement.human_or_replicant()
        captured = capsys.readouterr()
        assert captured.out == "Congratulations you are human!\n"
