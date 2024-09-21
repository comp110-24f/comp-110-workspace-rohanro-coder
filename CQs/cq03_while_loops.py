"""Using while loops to iterate over a string!"""

__author__ = "730476039"


def num_instances(phrase: str, search_char: str) -> int:
    """Finding the number of instances of a character in a string!"""
    count: int = 0
    index: int = 0
    while index < len(phrase):
        if search_char == phrase[index]:
            count += 1
            index += 1
        else:
            index += 1
    return count
