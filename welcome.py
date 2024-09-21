"""EX02 - Chardle - A cute step toward Wordle"""

__author__ = "730476039"


def input_word() -> str:
    """Asking users to input a word!"""
    five_character: str = input("Enter a 5-character word:")
    if len(five_character) == 5:
        return five_character
    else:
        print("Error: Word must contain 5 characters.")
        return five_character
