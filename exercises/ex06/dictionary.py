"""Dictionary utility functions!"""

__author__ = "730476039"


def invert(input: dict[str, str]) -> dict[str, str]:
    inverted: dict[str, str] = {}
    for elem in input:
        inverted[input[elem]] = elem
    if len(inverted) < len(input):
        raise KeyError("You used duplicate keys here!")
    return inverted


# I created a new variable called inverted that I assigned to an empty dictionary initially. In a for loop iterating through input, I did inverted[input[elem]] = elem because that would switch the keys and values. After that, for the condition for duplicate keys, I did len(inverted) < len(input) because python would remove one of the keys if there's a duplicate key.


def favorite_color(favcol: dict[str, str]) -> str:
    colnum: dict[str, int] = {}
    for elem in favcol:
        color: str = favcol[elem]
        if color in colnum:
            colnum[color] += 1
        else:
            colnum[color] = 1
    max_color: int = 0
    col: str = ""
    for elem in colnum:
        if colnum[elem] > max_color:
            max_color: int = colnum[elem]
            col: str = elem
    for elem in colnum:
        if colnum[elem] == max_color:
            return col
    return col


# I first initialized a new variable called colnum which is a dictionary where the keys are color (str) and the values are the number of times it is the favorite (int). Then, in a for loop, I created a variable called color that would be assigned to the value of the dictionary favcol. I counted that color in colnum based on whether we had seen it before or not. Then, I created two new variables, one with the color with the maximum votes and one with the actual number of votes that color got. In a for loop, I assigned those variables to the appropriate values with a conditional indicating whether the number in colnum was greater than or equal to the maximum number so far. To cycle through the list again and make sure the first color in the dictionary is picked in the case of a tie, I had to make the conditional colnum[elem] > max_color, and not put the greater than or equal to operator there.


def count(input: list[str]) -> dict[str, int]:
    num_list: dict[str, int] = {}
    for elem in input:
        if elem in num_list:
            num_list[elem] += 1
        else:
            num_list[elem] = 1
    return num_list


def alphabetizer(input: list[str]) -> dict[str, list[str]]:
    letter_dict: dict[str, list[str]] = {}
    for elem in input:
        if elem[0].lower() in letter_dict:
            letter_dict[elem[0]].append(elem)
        else:
            letter_dict[elem[0].lower()] = [elem.lower()]
    return letter_dict


# For alphabetizer, I initialized an empty dictionary letter_dict. I iterated through the input list with a for loop. I made it so that if the first letter was not already in the dictionary, I'd start a list with that element. If the first letter was already in the dictionary, I'd just append the value to the already created list.


def update_attendance(att: dict[str, list[str]], weekday: str, student: str) -> None:
    if weekday in att:
        att[weekday].append(student)
    else:
        att[weekday] = [student]
    print(att)


# I had to make an if-else statement for two conditions: if the weekday was already in att, in which case I would append something to the existing list, and if the weekday was not in the dictionary, in which case I'd create a new list.
