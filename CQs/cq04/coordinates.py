"""Coordinates!"""

__author__ = "730476039"


def get_coords(xs: str, ys: str) -> None:
    index_x: int = 0
    index_y: int = 0
    while index_x < len(xs):
        while index_y < len(ys):
            print("(" + xs[index_x] + "," + ys[index_y] + ")")
            index_y += 1
        index_x += 1
        index_y = 0
