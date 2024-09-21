"""EX02 - Chardle - A cute step toward Wordle"""

__author__ = "730476039"


def input_word() -> str:
    """Asking users to input a word!"""
    five_character: str = input("Enter a 5-character word: ")
    if len(five_character) == 5:
        return five_character
    else:
        print("Error: Word must contain 5 characters.")
        exit()
        return five_character


def input_letter() -> str:
    single_cha: str = input("Enter a single character: ")
    if len(single_cha) == 1:
        return single_cha
    else:
        print("Error: Character must be a single character.")
        exit()
        return single_cha


# For the contains_char() function, since the while loop we learned about is a forbidden construct, I had to use multiple if statements for indices 0-4 for whatever the word input was. Initially, I was worried about whether things from the previous two functions would show up, but I realized that if you make input_word() and input_letter() your arguments, this will happen.


def contains_char(word: str, letter: str) -> None:
    count_char: int = 0
    print("Searching for " + letter + " in " + word)
    if letter == word[0]:
        print(letter + " found at index 0")
        count_char += 1
    if letter == word[1]:
        print(letter + " found at index 1")
        count_char += 1
    if letter == word[2]:
        print(letter + " found at index 2")
        count_char += 1
    if letter == word[3]:
        print(letter + " found at index 3")
        count_char += 1
    if letter == word[4]:
        print(letter + " found at index 4")
        count_char += 1
    if count_char == 0:
        print("No instances of " + letter + " found in " + word)
    if count_char == 1:
        print("1 instance of " + letter + " found in " + word)
    else:
        print(str(count_char) + " instances of " + letter + " found in " + word)


# For part 4 of the exercise, I knew I had to put count_char += 1 in every if statement because if the condition of the if statement is True, count_char increases by 1. I had to create one more if statement and one else statement for the cases of count_char equals 0 and count_char does not equal 0, because they sought different outputs.


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
