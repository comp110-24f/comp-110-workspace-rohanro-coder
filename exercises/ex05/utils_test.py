"""Defining unit tests for list utility functions!"""

from exercises.ex05.utils import only_evens

from exercises.ex05.utils import sub

from exercises.ex05.utils import add_at_index

import pytest

__author__ = "730476039"


def test_evens_return() -> None:
    """Seeing if only_evens returns only even numbers."""
    assert only_evens([10, 21, 32, 43, 54]) == [10, 32, 54]


# I asserted a boolean expression here that confirms that the function returns a new list with only the even numbers from the original list.


def test_evens_mutate() -> None:
    """Seeing if only_evens doesn't mutate the original list."""
    a: list[int] = [10, 21, 32, 43, 54]
    only_evens(a)
    assert a == [10, 21, 32, 43, 54]


# I had to create another variable for the unchanged input list here because input is a local variable that was not recognized here.


def test_evens_edge() -> None:
    "Seeing if an empty list for only_evens works."
    a: list[int] = []
    assert only_evens(a) == []


def test_sub_return() -> None:
    """Seeing if sub returns a list from the start index to the end index - 1."""
    assert sub([5, 10, 15, 20, 25, 30], 1, 5) == [10, 15, 20, 25]


def test_sub_mutate() -> None:
    """Seeing if sub doesn't mutate the original list."""
    a: list[int] = [5, 10, 15, 20, 25, 30]
    sub(a, 1, 5)
    assert a == [5, 10, 15, 20, 25, 30]


def test_sub_edge() -> None:
    """Seeing if an empty list for sub works."""
    a: list[int] = []
    assert sub(a, 1, 3) == []


def test_add_at_index_return() -> None:
    """Seeing if add at index returns nothing."""
    assert add_at_index([2, 4, 8, 10], 6, 2) == None


def test_add_at_index_mutate() -> None:
    """Seeing if adding at index mutates the original list."""
    a: list[int] = [2, 4, 8, 10]
    add_at_index(a, 6, 2)
    assert a == [2, 4, 6, 8, 10]


def test_add_at_index_raises_indexerror():
    """Seeing if IndexError in add at index is raised correctly."""
    a: list[int] = [1, 2]
    with pytest.raises(IndexError):
        assert (
            add_at_index(a, 5, 10)
            == "IndexError: Index is out of bounds for the input list"
        )
