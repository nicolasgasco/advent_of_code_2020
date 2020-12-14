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
distance between that location and the ship's starting position?

--- Part Two ---
Before you can give the destination to the captain, you realize that the actual
action meanings were printed on the back of the instructions the whole time.

Almost all of the actions indicate how to move a waypoint which is relative to
the ship's position:

Action N means to move the waypoint north by the given value.
Action S means to move the waypoint south by the given value.
Action E means to move the waypoint east by the given value.
Action W means to move the waypoint west by the given value.
Action L means to rotate the waypoint around the ship left (counter-clockwise)
the given number of degrees.
Action R means to rotate the waypoint around the ship right (clockwise) the given
number of degrees.
Action F means to move forward to the waypoint a number of times equal to the
given value.
The waypoint starts 10 units east and 1 unit north relative to the ship. The
waypoint is relative to the ship; that is, if the ship moves, the waypoint moves
with it.

For example, using the same instructions as above:

F10 moves the ship to the waypoint 10 times (a total of 100 units east and 10
units north), leaving the ship at east 100, north 10. The waypoint stays 10
units east and 1 unit north of the ship.
N3 moves the waypoint 3 units north to 10 units east and 4 units north of the
ship. The ship remains at east 100, north 10.
F7 moves the ship to the waypoint 7 times (a total of 70 units east and 28
units north), leaving the ship at east 170, north 38. The waypoint stays 10
units east and 4 units north of the ship.
R90 rotates the waypoint around the ship clockwise 90 degrees, moving it to 4
units east and 10 units south of the ship. The ship remains at east 170, north 38.
F11 moves the ship to the waypoint 11 times (a total of 44 units east and 110
units south), leaving the ship at east 214, south 72. The waypoint stays 4 units
east and 10 units south of the ship.
After these operations, the ship's Manhattan distance from its starting position
is 214 + 72 = 286.

Figure out where the navigation instructions actually lead. What is the Manhattan
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

print(f"The result of the first part is: {abs_north_south + abs_east_west}.")


# Part 2

directions = ["north", "east", "south", "west"]
ship = {"north": 0, "east": 0, "south": 0, "west": 0}

# Waypoint initialized with other coordinates
waypoint = {"north": ship["north"]+1, "east": ship["east"]+10, "south": ship["south"], "west": ship["west"]}



# Iterate all instructions
for line in data:
	letter = line[0]
	value = int(line[1:])
	turns = int(value / 90)
	

	if letter == "N":
		waypoint["north"] += value

	elif letter == "S":
		waypoint["south"] += value

	elif letter == "E":
		waypoint["east"] += value

	elif letter == "W":
		waypoint["west"] += value

	elif letter == "R":
		# Copy necessary, otherwise you change one value and the next one reads
		# the new one and not the old one as it should be
		waypoint_copy = waypoint.copy()

		# Turning right is switching left all directions
		for direction in directions:
			waypoint[direction] = waypoint_copy[directions[(directions.index(direction) - turns)]]


	elif letter == "L":
		waypoint_copy = waypoint.copy()


		for direction in directions:
			# List can go out of range, therefore %
			waypoint[direction] = waypoint_copy[directions[(directions.index(direction) + turns) % len(directions)]]

	# Relative to waypoint
	elif letter == "F":

		# We're going north
		if waypoint["north"] != 0:

			# Current south value is bigger than movement
			if ship["south"] - (value * waypoint["north"]) >= 0:
				ship["north"] = 0
				ship["south"] = ship["south"] - (value * waypoint["north"])

			# Current south value is smaller than movement
			else:
				ship["north"] += abs(ship["south"] - (value * waypoint["north"]))
				ship["south"] = 0

		if waypoint["south"] != 0:
			if ship["north"] - (value * waypoint["south"]) >= 0:
				ship["south"] = 0
				ship["north"] = ship["north"] - (value * waypoint["south"])
			else:
				ship["south"] += abs(ship["north"] - (value * waypoint["south"]))
				ship["north"] = 0 

		if waypoint["west"] != 0:
			if ship["east"] - (value * waypoint["west"]) >= 0:
				ship["west"] = 0
				ship["east"] = ship["east"] - (value * waypoint["west"])
			else:
				ship["west"] += abs(ship["east"] - (value * waypoint["west"]))
				ship["east"] = 0 

		if waypoint["east"] != 0:
			if ship["west"] - (value * waypoint["east"]) >= 0:
				ship["east"] = 0
				ship["west"] = ship["west"] - (value * waypoint["east"])
			else:
				ship["east"] += abs(ship["west"] - (value * waypoint["east"]))
				ship["west"] = 0 	


abs_east_west = abs(ship["west"] - ship["east"])
abs_north_south = abs(ship["north"] - ship["south"])

print(f"The result of the second part is {abs_east_west + abs_north_south}.")