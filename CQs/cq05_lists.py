"""Mutating functions."""

__author__ = "730476039"


def manual_append(a: list[int], num: int) -> None:
    """Appending a list."""
    a.append(num)


def double(int_list: list[int]) -> None:
    """Doubling every item in a list of integers."""
    index: int = 0
    while index < len(int_list):
        int_list[index] *= 2
        index += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1
double(list_2)
print(list_1)
print(list_2)
