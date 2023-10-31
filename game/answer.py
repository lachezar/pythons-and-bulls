from typing import NewType, Self
from dataclasses import dataclass
from game.error import Error

Pythons = NewType("Pythons", int)
Bulls = NewType("Bulls", int)


@dataclass(slots=True, frozen=True)
class Answer:
    bulls: Bulls
    pythons: Pythons

    def validate(self: Self) -> Error | Self:
        if self.pythons < 0 or self.pythons > 4:
            return Error("Pythons must be between 0 and 4")
        elif self.bulls < 0 or self.bulls > 4:
            return Error("Bulls must be between 0 and 4")
        elif self.bulls + self.pythons > 4:
            return Error("Sum of pythons and bulls must be between 0 and 4")
        else:
            return self

    @classmethod
    def parse(cls, bulls_input: str, pythons_input: str) -> Error | Self:
        try:
            bulls = int(bulls_input.strip(), 10)
            pythons = int(pythons_input.strip(), 10)
            return cls(Bulls(bulls), Pythons(pythons)).validate()
        except:
            return Error("The bulls and pythons input must be integers")
