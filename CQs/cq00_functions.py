"""Functions challenge question!"""

__author__ = "730476039"


def mimic(message: str) -> str:
    """A function to take your input and repeat it back to you."""
    return message


def main() -> None:
    """Pulling together your functions."""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
