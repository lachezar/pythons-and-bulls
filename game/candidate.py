from typing import Self
from dataclasses import dataclass
from game.answer import *
from game.error import Error


@dataclass(slots=True, frozen=True)
class Candidate:
    a: int
    b: int
    c: int
    d: int

    def __to_list(self: Self) -> list[int]:
        return [self.a, self.b, self.c, self.d]

    def compare(self: Self, other: Self) -> Answer:
        from functools import reduce

        bulls = Bulls(
            reduce(
                lambda acc, elements: acc + 1 if elements[0] == elements[1] else acc,
                zip(self.__to_list(), other.__to_list()),
                0,
            )
        )
        pythons = Pythons(
            4 - len(set(self.__to_list()) - set(other.__to_list())) - bulls
        )
        return Answer(bulls, pythons)

    def validate(self: Self) -> Error | Self:
        if len(set(self.__to_list())) != 4:
            return Error("The number candidate must not contain repeating digits")
        elif self.a == 0:
            return Error("The number candidate must not start with 0")
        else:
            return self

    def __str__(self: Self) -> str:
        return "".join(map(str, self.__to_list()))

    @classmethod
    def parse(cls, candidate_input: str) -> Error | Self:
        try:
            digits = [int(char) for char in candidate_input.strip()]
            if len(digits) != 4:
                return Error("The input must be integer with 4 digits")
            return cls(digits[0], digits[1], digits[2], digits[3]).validate()
        except:
            return Error("The input must be integer")

    @classmethod
    def generate_candidates(cls) -> list[Self]:
        from itertools import permutations

        return [
            cls(c[0], c[1], c[2], c[3])
            for c in permutations(range(0, 10), 4)
            if c[0] != 0
        ]
