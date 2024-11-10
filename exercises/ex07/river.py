"""File to define River class."""

__author__ = "730476039"

from exercises.ex07.bear import Bear
from exercises.ex07.fish import Fish


class River:

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        modified_bear: list[Bear] = []
        for elem in self.bears:
            if elem.age <= 5:
                modified_bear.append(elem)
        self.bears = modified_bear
        modified_fish: list[Fish] = []
        for elem in self.fish:
            if elem.age <= 3:
                modified_fish.append(elem)
        self.fish = modified_fish

        return None

    # For check_ages, I had to do elem.age for both bears.age instead of Bear.age because it was about modifying the elements in the lists, not modifying the whole class. That confused me for a while.

    def bears_eating(self):
        for elem in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                elem.eat(3)
        return None

    # For the bears_eating method, I had to iterate through the bears list with a for loop and make a conditional that would be true if there are 5 fish or greater. It was necessary to both remove the fish and update the bears' hunger_score.

    def check_hunger(self):
        new_bears: list[Bear] = []
        for elem in self.bears:
            if elem.hunger_score >= 0:
                new_bears.append(elem)
        new_bears = self.bears

    def repopulate_fish(self):
        for new_fish in range((len(self.fish) // 2) * 4):
            self.fish.append(Fish())
        return None

    def repopulate_bears(self):
        for new_bear in range(len(self.bears) // 2):
            self.bears.append(Bear())
        return None

    # For repopulate_fish and repopulate_bears, I was confused becaue new_fish and new_bear weren't used, but in reality we don't care about elemetns of the list here as much as the numbers and adding new offspring.

    def view_river(self) -> None:
        print(f"~~~ Day {self.day}~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    # For view_river, I initially just did Fish population: self.fish in the f-string, but it was the len function that would actually give me the length of those organisms in the output.

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()

    def remove_fish(self, amount: int):
        x: int = 0
        while x < amount:
            self.fish.pop(x)
            x += 1
