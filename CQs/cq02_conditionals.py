"""Practice with conditionals, local variables, and user input!"""

__author__ = "730476039"


def guess_a_number() -> None:
    """Guessing game."""
    secret: int = 7
    x: int = int(input("Guess a number: "))
    print("Your guess was " + str(x))
    if x == 7:
        print("You got it!")
    elif x < 7:
        print("Your guess was too low! The secret number is 7")
    else:
        print("Your guess was too high! The secret number is 7")


if __name__ == "__main__":
    guess_a_number()
