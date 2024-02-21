import unittest


class Key:
    def __init__(self, passphrase) -> None:
        self.passphrase = passphrase

    def __len__(self):
        return 1337

    def __getitem__(self, index):
        if index == 404:
            return 3
        raise ("index out of range")

    def __gt__(self, value):
        return value < 10000

    def __str__(self) -> str:
        return "GeneralTsoKeycard"


class TestStringMethods(unittest.TestCase):

    def test_0(self):
        key = Key("zax2rulez")
        self.assertTrue(len(key) == 1337)
        self.assertTrue(key[404] == 3)
        self.assertTrue(key > 9000)
        self.assertTrue(key.passphrase == "zax2rulez")
        self.assertTrue(str(key) == "GeneralTsoKeycard")


if __name__ == "__main__":
    unittest.main()
