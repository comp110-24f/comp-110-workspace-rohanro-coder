"""File to define Fish class."""

__author__ = "730476039"


class Fish:
    age: int

    def __init__(self):
        self.age = 0
        return None

    def one_day(self):
        self.age += 1
        return None
