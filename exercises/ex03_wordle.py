"""Wordle game!"""

__author__ = "730476039"


def input_guess(num_char: int) -> str:
    """Prompting the user to input a word of a certain length."""
    first_prompt: str = input(f"Enter a {num_char} character word: ")
    while len(first_prompt) != num_char:
        first_prompt = input(f"That wasn't {num_char} chars! Try again: ")
    return first_prompt


# I had to use f strings and the input function for both the initial prompts and the try again prompt because it had num_char and needed to ask the user for an input. The conditional was len(first_prompt) not being equal to num_char, which would result in the try again statement. If they were equal, the first_prompt value would simply be returned.


def contains_char(word: str, single_char: str) -> bool:
    """Seeing if a word contains a certain character."""
    assert len(single_char) == 1
    index: int = 0
    presence: bool = False
    while index < len(word):
        if single_char == word[index]:
            presence = True
        index += 1
    return presence


# I made a variable called index that would increase in the while loop as we examined every single letter of word. I made a variable called presence which is the bool False, that changes to True if the single_char is found in word.


def emojified(guess: str, secret_word: str) -> str:
    """Representing the accuracy of a guess in relation to a secret word."""
    assert len(guess) == len(secret_word)
    white_box: str = "\U00002B1C"
    green_box: str = "\U0001F7E9"
    yellow_box: str = "\U0001F7E8"
    index_guess: int = 0
    emoji: str = ""
    while index_guess < len(guess):
        if contains_char(secret_word, guess[index_guess]):
            if guess[index_guess] == secret_word[index_guess]:
                emoji += green_box
            else:
                emoji += yellow_box
        else:
            emoji += white_box
        index_guess += 1
    return emoji


# Initially, I thought I could just put things like return green_box, but that made parts of the code unreachable. Therefore, I made a variable called emoji, that was initially an empty string, to which green, yellow, or white boxes were added if certain conditions were met. When applying the contains_char() function here, I initially did contains_char(arguments) == True, when in reality I just needed contains_char(arguments), because the conditional would evaluate to if True or if False. I realized that the yellow_box and green_box both required contains_char() to be true, so I made a nested if statement to execute those. When I initially tried if, elif, else, the code did not work.


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    while turn < 7:
        print(f"=== Turn {turn}/6 ===")
        user_word: str = input_guess(num_char=len(secret))
        print(emojified(guess=user_word, secret_word=secret))
        if user_word == secret:
            print(f"You won in {turn}/6 turns!")
            return None
        if turn == 6 and user_word != secret:
            print("X/6 - Sorry, try again tomorrow!")
        turn += 1


# I created a new variable here called turn representing the turn number a given player is on, as well as a new variable called user_word that is assigned as someone's input into the program. I used the input_guess function with keyword argument, where num_char = len(secret), so the program knows how many characters the word should be. I then used the emoijified function with keyword argument where guess was equal to user_word and secret_word was equal to secret. I had to put return None in the then block of if user_word == secret, otherwise the program went on to the next turn, even when I won.

if __name__ == "__main__":
    main(secret="codes")
