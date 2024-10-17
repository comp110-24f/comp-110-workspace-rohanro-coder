"""Practice with Unit Tests!"""

__author__ = "730476039"


def find_and_remove_max(numbers: list[int]) -> int:
    if numbers == []:
        return -1
    value: int = numbers[0]
    for elem in numbers:
        if elem > value:
            value = elem
        else:
            value = value
    find: int = 0
    while find < len(numbers):
        if numbers[find] == value:
            numbers.pop(find)
        else:
            find += 1
    return value


a: list[int] = [4, 5, 9, 3, 1]

print(find_and_remove_max(numbers=a))

print(a)
