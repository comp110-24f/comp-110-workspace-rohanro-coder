"""Practice with Unit Tests!"""

from CQs.cq07.find_max import find_and_remove_max

__author__ = "730476039"

a: list[int] = [4, 5, 9, 3, 1]


def test_return_expected() -> None:
    assert find_and_remove_max(numbers=a) == 9


def test_mutate_expected() -> None:
    find_and_remove_max(numbers=a)
    assert a == [4, 5, 3, 1]


b: list[int] = []


def test_unconventional() -> None:
    assert find_and_remove_max(numbers=[]) == -1
