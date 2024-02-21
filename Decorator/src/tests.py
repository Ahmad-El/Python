from functional_purse import *
from specific_decoration import *
from split_booty import *

import unittest


class TestMyModule(unittest.TestCase):
    def test_ex00(self):
        purse: dict[str, int] = {}
        self.assertEqual(empty(purse).get("gold_ingots"), 0)
        purse = add_ingot(get_ingot(add_ingot(empty(purse))))
        self.assertEqual(purse.get("gold_ingots"), 1)

    def test_ex01_0(self):
        purses: tuple(dict[str, int])
        purses = spllit_booty(
            {"gold_ingots": 3},
            {"gold_ingots": 2},
            {"apples": 10})
        self.assertEqual(get_value(purses[0]), 2)
        self.assertEqual(get_value(purses[1]), 2)
        self.assertEqual(get_value(purses[2]), 1)

    def test_ex01_1(self):
        purses: tuple(dict[str, int])
        purses = spllit_booty(
            {"gold_ingots": 3}, {"gold_ingots": 9}, {"gold_ingots": 1}
        )
        self.assertEqual(get_value(purses[0]), 5)
        self.assertEqual(get_value(purses[1]), 4)
        self.assertEqual(get_value(purses[2]), 4)


if __name__ == "__main__":
    unittest.main()
