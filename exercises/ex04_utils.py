"""List utility functions!"""

__author__ = "730476039"


def all(list_int: list[int], num: int) -> bool:
    """Seeing if all of a list is equal to a certain number."""
    test: bool = True
    for elem in list_int:
        if elem == num:
            test = True
        else:
            test = False
            return test
    return test


# I knew I had to create a variable with the possible boolean values, True and False, because that is what the function should return. I created an if else statement that would differentiate between the scenarios where every number in the list was equal to the integer and where they were not. I had to place one return statement inside the else block in order to exit the function at the appropriate time.


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
    equal: bool = True
    if list_1 == list_2:
        equal = equal
    else:
        equal = False
    return equal


def extend(list_1: list[int], list_2: list[int]) -> None:
    """Appending the second list to the first list."""
    list_1 += list_2


# I initially wanted to use the append function here, but list_2 was not an accepted argument. Therefore, I just used += like you do to change a variable.
