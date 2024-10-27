"""Writing list utility functions!"""

__author__ = "730476039"


def only_evens(input: list[int]) -> list[int]:
    """Returning only the even elements of the list."""
    even: list[int] = []
    for elem in input:
        if elem % 2 == 0:
            even.append(elem)
    return even


# I had to use the modulo operator with a divisor of 2 to make the condition that a given element in a list was even.


def sub(input: list[int], idx_start: int, idx_end: int) -> list[int]:
    """Returning the start to the end of the list (non-inclusive)."""
    new_list: list[int] = []
    idx_s: int = idx_start
    idx_e: int = idx_end
    if len(input) == 0:
        return new_list
    if idx_s > len(input):
        return input
    if idx_s == len(input):
        return []
    if idx_end <= 0:
        return input
    if idx_start < 0:
        idx_s = 0
    if idx_end > len(input):
        idx_e = len(input)
    while idx_s < idx_e:
        new_list.append(input[idx_s])
        idx_s += 1
    return new_list


# I had to put a bunch of if statements for special conditions where input is an empty list, the start of the index is greater than the length of the list, the end index is 0 or below, the start index is less than 0, and the end index is greater than the length of the list. I created new variables for the start and end indexes, and then appended the correct values to my new list with that in a while loop.


def add_at_index(input: list[int], number: int, idx: int) -> None:
    """Adding a number at a given index in a list."""
    if idx < 0 or idx > len(input):
        raise IndexError("Index is out of bounds for the input list")
    index: int = len(input) - 1
    end_list: list[int] = []
    while index >= idx:
        end_list.append(input[index])
        input.pop(index)
        index -= 1
    input.append(number)
    idx_end: int = len(end_list) - 1
    while idx_end >= 0:
        input.append(end_list[idx_end])
        idx_end -= 1
    print(input)


# I made a variable index that was equal to the length of the list - 1, and did a while loop where I kept decreasing it until it reached the index value. During the while loop, I popped everything and saved everything I removed to a new list called end_list. Then, I could use append to get number in the correct position. After that, I used a while loop to go thorugh every element of end_list backwards, in order to append that to input as well.
