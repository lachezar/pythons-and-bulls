import unittest
from game.answer import *


class TestAnswer(unittest.TestCase):
    def test_answer_parsing(self):
        self.assertFalse(
            isinstance(Answer.parse("", ""), Answer),
        )
        self.assertFalse(
            isinstance(Answer.parse("2", "3"), Answer),
        )
        self.assertFalse(
            isinstance(Answer.parse("5", "0"), Answer),
        )
        self.assertFalse(
            isinstance(Answer.parse("-3", "2"), Answer),
        )
        self.assertEqual(Answer.parse("1 ", " 2"), Answer(Bulls(1), Pythons(2)))


if __name__ == "__main__":
    unittest.main()
