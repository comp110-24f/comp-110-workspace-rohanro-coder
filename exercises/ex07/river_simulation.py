"File to actually execute things in the river simulation."

from exercises.ex07.river import River

__author__ = "730476039"

my_river: River = River(10, 2)
my_river.view_river()
my_river.one_river_week()
