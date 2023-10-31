import unittest
from game.candidate import *
from game.answer import *


class TestCandidate(unittest.TestCase):
    def test_candidates_generation(self):
        candidates = Candidate.generate_candidates()
        self.assertEqual(
            len(candidates),
            (10 - 1) * 9 * 8 * 7,  # number of candidates: 10!/6! - 9!/6!
            "The generated candidates are not complete",
        )
        self.assertEqual(candidates[0], Candidate(1, 0, 2, 3))
        self.assertEqual(candidates[len(candidates) - 1], Candidate(9, 8, 7, 6))

    def test_candidates_comparison(self):
        self.assertEqual(
            Candidate(1, 2, 3, 4).compare(Candidate(2, 1, 3, 4)),
            Answer(Bulls(2), Pythons(2)),
        )
        self.assertEqual(
            Candidate(1, 2, 3, 4).compare(Candidate(1, 9, 3, 0)),
            Answer(Bulls(2), Pythons(0)),
        )
        self.assertEqual(
            Candidate(1, 2, 3, 4).compare(Candidate(4, 3, 2, 1)),
            Answer(Bulls(0), Pythons(4)),
        )

    def test_candidates_parsing(self):
        self.assertFalse(
            isinstance(Candidate.parse(""), Candidate),
        )
        self.assertFalse(
            isinstance(Candidate.parse("1231"), Candidate),
        )
        self.assertFalse(
            isinstance(Candidate.parse("0123"), Candidate),
        )
        self.assertFalse(
            isinstance(Candidate.parse("12345"), Candidate),
        )
        self.assertEqual(Candidate.parse(" 1234 "), Candidate(1, 2, 3, 4))
        self.assertEqual(Candidate.parse("5678"), Candidate(5, 6, 7, 8))


if __name__ == "__main__":
    unittest.main()
