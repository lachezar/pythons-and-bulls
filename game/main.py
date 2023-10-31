from game.error import Error
from game.candidate import *
from game.answer import *


def game_loop() -> None:
    import random

    candidates: list[Candidate] = Candidate.generate_candidates()
    computers_number: Candidate = random.choice(candidates)
    while True:
        while True:
            inp = input("Ask the computer for its number: ")
            result = Candidate.parse(inp)
            if isinstance(result, Candidate):
                computer_answer = computers_number.compare(result)
                print(
                    f"Bulls: {computer_answer.bulls}, Pythons: {computer_answer.pythons}"
                )

                if computer_answer.bulls == 4:
                    print()
                    print("You won!!!")
                    return

                break
            else:
                print(f"Input error: {result}; Try again!")

        computers_query: Candidate = random.choice(candidates)

        while True:
            print(f"The computer asks for your number: {computers_query}")
            inp_bulls = input("How many bulls: ")
            inp_pythons = input("How many pythons: ")
            answer: Error | Answer = Answer.parse(inp_bulls, inp_pythons)

            if isinstance(answer, Answer):
                if answer.bulls == 4:
                    print()
                    print("The computer won!!!")
                    return

                candidates = [
                    c for c in candidates if answer == computers_query.compare(c)
                ]

                if len(candidates) == 0:
                    print()
                    print(
                        "There are no possible numbers matching your answers! The computer is sad :("
                    )
                    return

                break
            else:
                print(f"Input error: {answer}; Try again!")


if __name__ == "__main__":
    game_loop()
