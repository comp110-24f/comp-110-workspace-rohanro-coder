"""This program will plan for a tea party!"""

__author__: str = "730476039"


def main_planner(guests: int) -> None:
    """This is the entrypoint of the program which will bring all of our tea party functions together."""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))


# For the main_planner function I concatenated strings by putting different strings together with the + sign. I made sure spacing in the strings was adequate so the program would print neatly. I had to change some int and float outputs to strings with str() so that it would run.


def tea_bags(people: int) -> int:
    """Calculating number of tea bags needed based on number of guests."""
    return 2 * people


def treats(people: int) -> int:
    """Computing treats needed based on number of teas."""
    return int(1.5 * tea_bags(people=1) * people)


# For the treats function, I did 1.5 * tea_bags(people) because I didn't directly have the teas information. Furthermore, I had to surround the return statement with int to make it an integer because it would return a float otherwise.


def cost(tea_count: int, treat_count: int) -> float:
    """Calculating the cost of the tea bags and treats."""
    return 0.5 * tea_count + 0.75 * treat_count


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
