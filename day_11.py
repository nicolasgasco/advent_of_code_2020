"""--- Day 11: Seating System ---
Your plane lands with plenty of time to spare. The final leg of your journey is
a ferry that goes directly to the tropical island where you can finally start
your vacation. As you reach the waiting area to board the ferry, you realize
you're so early, nobody else has even arrived yet!

By modeling the process people use to choose (or abandon) their seat in the
waiting area, you're pretty sure you can predict the best place to sit. You make
a quick map of the seat layout (your puzzle input).

The seat layout fits neatly on a grid. Each position is either floor (.), an
empty seat (L), or an occupied seat (#). For example, the initial seat layout
might look like this:

L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL
Now, you just need to model the people who will be arriving shortly. Fortunately,
people are entirely predictable and always follow a simple set of rules. All
decisions are based on the number of occupied seats adjacent to a given seat
(one of the eight positions immediately up, down, left, right, or diagonal from
the seat). The following rules are applied to every seat simultaneously:

If a seat is empty (L) and there are no occupied seats adjacent to it, the seat
becomes occupied.
If a seat is occupied (#) and four or more seats adjacent to it are also
occupied, the seat becomes empty.

Otherwise, the seat's state does not change.
Floor (.) never changes; seats don't move, and nobody sits on the floor.

After one round of these rules, every seat in the example layout becomes
occupied:

#.##.##.##
#######.##
#.#.#..#..
####.##.##
#.##.##.##
#.#####.##
..#.#.....
##########
#.######.#
#.#####.##
After a second round, the seats with four or more occupied adjacent seats
become empty again:

#.LL.L#.##
#LLLLLL.L#
L.L.L..L..
#LLL.LL.L#
#.LL.LL.LL
#.LLLL#.##
..L.L.....
#LLLLLLLL#
#.LLLLLL.L
#.#LLLL.##
This process continues for three more rounds:

#.##.L#.##
#L###LL.L#
L.#.#..#..
#L##.##.L#
#.##.LL.LL
#.###L#.##
..#.#.....
#L######L#
#.LL###L.L
#.#L###.##
#.#L.L#.##
#LLL#LL.L#
L.L.L..#..
#LLL.##.L#
#.LL.LL.LL
#.LL#L#.##
..L.L.....
#L#LLLL#L#
#.LLLLLL.L
#.#L#L#.##
#.#L.L#.##
#LLL#LL.L#
L.#.L..#..
#L##.##.L#
#.#L.LL.LL
#.#L#L#.##
..L.L.....
#L#L##L#L#
#.LLLLLL.L
#.#L#L#.##
At this point, something interesting happens: the chaos stabilizes and further
applications of these rules cause no seats to change state! Once people stop
moving around, you count 37 occupied seats.

Simulate your seating area by applying the seating rules repeatedly until no
seats change state. How many seats end up occupied?"""

file = "day_11_input.txt"

with open(file) as f:
	lines = f.readlines()
	lines = [line.rstrip() for line in lines]


data = []
for line in lines:
	new_line = []
	for char in line:
		new_line.append(char)
	data.append(new_line)


def from_list_to_string(data):
	"""Convert a list of lists in a list of strings"""
	new_data = []
	for list in data:
		string = ""
		for el in list:
			string += el

		new_data.append(string)

	return new_data


def get_new_configuration(data):
	"""Applies rules once to the all the seats"""
	new_new_data = []
	y = 0
	while y < len(data):


		x = 0
		new_new_line = []
		while x < len(data[y]):

			if 1 <= y < len(data)-1 and 1 <= x < len(data[y])-1:
				one_right = data[y][x+1]
				one_left = data[y][x-1]
				one_down = data[y+1][x]
				one_up = data[y-1][x]
				one_down_right = data[y+1][x+1]
				one_down_left = data[y+1][x-1]
				one_up_right = data[y-1][x+1]
				one_up_left = data[y-1][x-1]

			# Upper left corner
			elif x-1 < 0 and y-1 < 0:
				one_right = data[y][x+1]
				one_left = "."
				one_down_right = data[y+1][x+1]
				one_down_left = "."
				one_up_right = "."
				one_up_left = "."
				one_down = data[y+1][x]
				one_up = "."

			# Bottom left corner
			elif x-1 < 0 and y+1 >= len(data):
				one_right = data[y][x+1]
				one_left = "."
				one_down_right = "."
				one_down_left = "."
				one_up_right = data[y-1][x+1]
				one_up_left = "."
				one_down = "."
				one_up = data[y-1][x]
				
				
			# Upper right corner
			if x+1 >= len(data[y]) and y-1 < 0:
				one_right = "."
				one_left = data[y][x-1]
				one_down = data[y+1][x]
				one_up = "."
				one_down_right = "."
				one_down_left = data[y+1][x-1]
				one_up_right = "."
				one_up_left = "."

			# Bottom right corner
			if x+1 >= len(data[y]) and y+1 >= len(data):
				one_right = "."
				one_left = data[y][x-1]
				one_down = "."
				one_up = data[y-1][x]
				one_down_right = "."
				one_down_left = "."
				one_up_right = "."
				one_up_left = data[y-1][x-1]

			# Left side
			if x-1 < 0 and 1 <= y < len(data)-1:
				one_right = data[y][x+1]
				one_left = "."
				one_down = data[y+1][x]
				one_up = data[y-1][x]
				one_down_right = data[y+1][x+1]
				one_down_left = "."
				one_up_right = data[y-1][x+1]
				one_up_left = "."

			# Right side
			elif x+1 >= len(data[y]) and 1 <= y < len(data)-1:
				one_right = "."
				one_down_right = "."
				one_up_right = "."
				one_left = data[y][x-1]
				one_down = data[y+1][x]
				one_up = data[y-1][x]
				one_down_left = data[y+1][x-1]
				one_up_left = data[y-1][x-1]

			# Upper side
			elif y-1 < 0 and 1 <= x < len(data[y])-1:
				one_up = "."
				one_down_left = data[y+1][x-1]
				one_down_right = data[y+1][x+1]
				one_right = data[y][x+1]
				one_left = data[y][x-1]
				one_down = data[y+1][x]
				one_up_right = "."
				one_up_left = "."

			# Bottom side
			elif y+1 > len(data)-1 and 1 <= x < len(data[y])-1:
				one_down = "."
				one_up_right = data[y-1][x+1]
				one_up_left = data[y-1][x-1]
				one_right = data[y][x+1]
				one_left = data[y][x-1]
				one_up = data[y-1][x]
				one_down_right = "."
				one_down_left = "."


			string = one_left + one_right + one_down + one_up + one_down_right + one_down_left + one_up_right + one_up_left

			if data[y][x] == "L" and "#" not in string:
				new_new_line.append("#")

			elif data[y][x] == "#" and string.count('#') >= 4:
				new_new_line.append("L")

			else:
				new_new_line.append(data[y][x])


	
			x += 1
		new_new_data.append(new_new_line)

		y += 1

	return from_list_to_string(new_new_data)


def from_list_to_string(list):
	"""Transform a list of lists in a list of strings"""
	new_list = []
	for element in list:
		new_string = ""
		for char in element:
			new_string += char

		new_list.append(new_string)

	return new_list



def count_occupied_seats(data):
	"""Count the number of occupied seats"""
	occupied_seats = 0
	for row in data:
		occupied_seats += row.count("#")

	return occupied_seats


def calculate_first_result(data):
	"""Repeat function till result doesn't change and count occupied seats"""

	compare = [["example1"], ["example2"]]
	z = 0
	while compare[z] != compare[z-1]:
		result = get_new_configuration(data)
		compare.append(result)
		data = result	
		z += 1
	print(z)

	final_result = count_occupied_seats(result)

	return final_result


print(f"The result of the first half is {calculate_first_result(data)}.")




# Part 2

def get_newest_configuration(data):
	"""Applies rules once to the all the seats"""
	final_result = []

	# For every line in the list
	for y in range(len(data)):

		line_result = []

		#For every element of every line
		for x in range(len(data[y])):

			# If it's a dot, ignore
			if data[y][x] != ".":
				

				all_around = []

				loop = True
				# 8 like the eight directions in which to look
				for i in range(8):
					
					# Go to the right
					if i == 0:
						n = 1
						loop = True
						while loop:

							# If number is positive, try is enough
							try:
								all_right = data[y][x+n]
								if all_right != ".":
									all_around.append(all_right)
									loop = False
								else:
									n += 1
							except IndexError:
								all_around.append("?")
								loop = False

					# Go to the left
					elif i == 1:
						n = 1
						loop = True
						while loop:
							# Condition necessary, otherwise false positive
							if x-n >= 0: 
								all_left = data[y][x-n]
								if all_left != ".":
									all_around.append(all_left)
									loop = False
								else:
									n += 1
							else:
								all_around.append("?")
								loop = False

					# Go down
					elif i == 2:
						n = 1
						loop = True
						while loop:
							try:
								all_down = data[y+n][x]
								if all_down != ".":
									all_around.append(all_down)
									loop = False
								else:
									n += 1
							except IndexError:
								all_around.append("?")
								loop = False

					# Go up
					elif i == 3:
						n = 1
						loop = True
						while loop:
							if y-n >= 0:
								one_up = data[y-n][x]
								if one_up != ".":
									all_around.append(one_up)

									loop = False
								else:
									n += 1
							else:
								all_around.append("?")
								loop = False

					# Go diagonal down/right
					elif i == 4:
						n = 1
						loop = True
						while loop:
							try:
								one_down_right = data[y+n][x+n]
								if one_down_right != ".":
									all_around.append(one_down_right)
									loop = False
								else:
									n += 1
							except IndexError:
								all_around.append("?")
								loop = False

					# Go diagonal down/left
					elif i == 5:
						n = 1
						loop = True
						while loop:
							if x-n >= 0:
								try:
									one_down_left = data[y+n][x-n]
									if one_down_left != ".":
									 	all_around.append(one_down_left)
									 	loop = False
									else:
										n += 1
								except IndexError:
									all_around.append("?")
									loop = False
							else:
								all_around.append("?")
								loop = False		

					# Go diagonal up/right
					elif i == 6:
						n = 1
						loop = True
						while loop:
							if y-n >= 0:
								try:
									one_up_right = data[y-n][x+n]
									if one_up_right != ".":
										all_around.append(one_up_right)
										loop = False
									else:
										n += 1
								except IndexError:
									all_around.append("?")
									loop = False
							else:
								all_around.append("?")
								loop = False

					# Go diagonal up/left
					elif i == 7:
						n = 1
						loop = True
						while loop:
							if y-n >=0 and x-n >= 0:
								one_up_left = data[y-n][x-n]
								if one_up_left != ".":
									all_around.append(one_up_left)
									loop = False
								else:
									n += 1
							else:
								all_around.append("?")
								loop = False

				# If L and no # around -> L
				if data[y][x] == "L" and "#" not in all_around:
					line_result.append("#")

				# If # and 5 or more # around -> L
				elif data[y][x] == "#" and all_around.count('#') >= 5:
					line_result.append("L")
				# Do nothing
				else:
					line_result.append(data[y][x])

			# Dots are just copied over
			else:
				line_result.append(data[y][x])


		final_result.append(line_result)


	return  final_result

def calculate_second_result(data):
	"""Apply function until result doesn't change and return number of seats"""

	# Necessary initialize it with two
	compare = [["example1"], ["example2"]]
	z = 0
	# When two are identical, stop
	while compare[z] != compare[z-1]:

		result = get_newest_configuration(data)
		compare.append(result)
		# Do it over and over
		data = result
		z += 1

	final_result = count_occupied_seats(result), z

	return final_result


print(f"The result of the second half is {calculate_second_result(data)[0]} after {calculate_second_result(data)[1]} cycles.")



