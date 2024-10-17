"""List utility functions!"""

__author__ = "730476039"


def all(list_int: list[int], num: int) -> bool:
    """Seeing if all of a list is equal to a certain number."""
    test: bool = False
    for elem in list_int:
        if len(list_int) == 0:
            test = False
            return test
        elif elem == num:
            test = True
        else:
            test = False
            return test
    return test


# I knew I had to create a variable with the possible boolean values, True and False, because that is what the function should return. I created an if else statement that would differentiate between the scenarios where every number in the list was equal to the integer and where they were not. I had to place one return statement inside the else block in order to exit the function at the appropriate time. I put an if length of the list is 0 in the case of an empty list.


def max(list_int: list[int]) -> int:
    """Getting the max value of a list as output."""
    if len(list_int) == 0:
        raise ValueError("max() arg is an empty List")
    value: int = list_int[0]
    for elem in list_int:
        if elem > value:
            value = elem
        else:
            value = value
    return value


# I created a variable which I assigned to the first element of the list. In a for in loop, I changed value to be a given element if it was bigger, but kept it constant if it was not. I debated whether to use a while loop here, but then I would need to create an index variable and keep track of that.


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Seeing if two lists are equal at all indexes."""
    idx: int = 0
    if len(list_1) != len(list_2):
        return False
    while idx < len(list_1):
        if list_1[idx] != list_2[idx]:
            return False
        idx += 1
    return True


# To check if the lists were equal at every index, I did a while loop iterating through every index, putting a return statement in the else column in case that was not true. I had to an if statement with the conditional where the lengths of the lists were not equal to each other because otherwise it was like the function only considered lists with the same length.


def extend(list_1: list[int], list_2: list[int]) -> None:
    """Appending the second list to the first list."""
    idx: int = 0
    while idx < len(list_2):
        list_1.append(list_2[idx])
        idx += 1


# Appending a whole list did not work, so I just iterated through every index with a while loop so that I could use the append function.
