"""--- Day 12: Rain Risk ---
Your ferry made decent progress toward the island, but the storm came in faster
than anyone expected. The ferry needs to take evasive actions!

Unfortunately, the ship's navigation computer seems to be malfunctioning; rather
than giving a route directly to safety, it produced extremely circuitous
instructions. When the captain uses the PA system to ask if anyone can help, you
quickly volunteer.

The navigation instructions (your puzzle input) consists of a sequence of
single-character actions paired with integer input values. After staring at them
for a few minutes, you work out what they probably mean:

Action N means to move north by the given value.
Action S means to move south by the given value.
Action E means to move east by the given value.
Action W means to move west by the given value.
Action L means to turn left the given number of degrees.
Action R means to turn right the given number of degrees.
Action F means to move forward by the given value in the direction the ship is
currently facing.
The ship starts by facing east. Only the L and R actions change the direction
the ship is facing. (That is, if the ship is facing east and the next
instruction is N10, the ship would move north 10 units, but would still move
east if the following action were F.)

For example:

F10
N3
F7
R90
F11
These instructions would be handled as follows:

F10 would move the ship 10 units east (because the ship starts by facing east)
to east 10, north 0.
N3 would move the ship 3 units north to east 10, north 3.
F7 would move the ship another 7 units east (because the ship is still facing
east) to east 17, north 3.
R90 would cause the ship to turn right by 90 degrees and face south; it remains
at east 17, north 3.
F11 would move the ship 11 units south to east 17, south 8.
At the end of these instructions, the ship's Manhattan distance (sum of the
absolute values of its east/west position and its north/south position) from its
starting position is 17 + 8 = 25.

Figure out where the navigation instructions lead. What is the Manhattan
distance between that location and the ship's starting position?"""

file = "day_12.txt"
with open(file) as f:
	lines = f.readlines()

data = [line.rstrip() for line in lines]

directions = ["east", "south", "west", "north"]

current_position = {"north": 0, "east": 0, "south": 0, "west": 0, "current_direction": directions[0]}

# Iterate all instructions
for line in data:
	letter = line[0]
	value = int(line[1:])
	turns = int(value / 90)
	

	if letter == "N":
		current_position["north"] += value

	elif letter == "S":
		current_position["south"] += value

	elif letter == "E":
		current_position["east"] += value

	elif letter == "W":
		current_position["west"] += value

	elif letter == "R":
		
		index_current_direction = directions.index(current_position["current_direction"])
	
		current_position["current_direction"] = directions[(turns + index_current_direction) % len(directions)]


	elif letter == "L":

		index_current_direction = directions.index(current_position["current_direction"])
		current_position["current_direction"] = directions[index_current_direction - turns]

	elif letter == "F":
		direction = current_position["current_direction"]
		current_position[direction] += value

abs_north_south = abs(current_position['north'] - current_position['south'])
abs_east_west = abs(current_position['west'] - current_position['east'])

print(current_position["current_direction"])

print(f"The result of the first part is: {abs_north_south + abs_east_west}.")