"""With the toboggan login problems resolved, you set off toward the airport.
While travel by toboggan might be easy, it's certainly not safe: there's very
minimal steering and the area is covered in trees. You'll need to see which
angles will take you near the fewest trees.

Due to the local geology, trees in this area only grow on exact integer
coordinates in a grid. You make a map (your puzzle input) of the open squares (.)
and trees (#) you can see. For example:

..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
These aren't the only trees, though; due to something you read about once
involving arboreal genetics and biome stability, the same pattern repeats
to the right many times:

..##.........##.........##.........##.........##.........##.......  --->
#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........#.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...##....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#  --->
You start on the open square (.) in the top-left corner and need to reach
the bottom (below the bottom-most row on your map).

The toboggan can only follow a few specific slopes (you opted for a cheaper
model that prefers rational numbers); start by counting all the trees
you would encounter for the slope right 3, down 1:

From your starting position at the top-left, check the position
that is right 3 and down 1. Then, check the position that is right 3
and down 1 from there, and so on until you go past the bottom of the map.

The locations you'd check in the above example are marked here with O
where there was an open square and X where there was a tree:

..##.........##.........##.........##.........##.........##.......  --->
#..O#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....X..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#O#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..X...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.X#.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#.O..#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........X.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.X#...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...#X....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...X.#.#..#...#.#.#..#...#.#.#..#...#.#  --->
In this example, traversing the map using this slope would cause you
to encounter 7 trees.

Starting at the top-left corner of your map and following a slope
of right 3 and down 1, how many trees would you encounter?

To begin, get your puzzle input."""

def _list_from_file(file):
	"""Create a list from a file"""
	with open(file) as f:
		new_list = []
		lines = f.readlines()
	
	for line in lines:
		line = line.rstrip()
		# This is an approximation
		line = line * len(lines)
		new_list.append(line)

	return new_list


def count_trees(lst, line_multiplier, row_multiplier=1):
	"""Count the number of # symbols met on the way"""
	total_count = 0
	for i in range(len(lst)):
		# Multiplier for row increases bigger than 1
		i = i * row_multiplier

		# Starting position, multiplier won't affect it
		if i == 0:
			symbol = lst[0][0]

		# From row 2 on, position n * multiplier
		elif i < len(lst):
			symbol = lst[i][i*line_multiplier]

		# Last row is exception, second condition if in order not to skip it
		elif i == (len(lst) -1) or i > (len(lst) -1):
			symbol = lst[-1][(len(lst)*line_multiplier)-1]
			# This must be here for the break statement to work
			if symbol == "#":
				total_count += 1
			# Necessary otherwise it can be skipped
			break

		if symbol == "#":
			total_count += 1
	return total_count

def multiply_results(result1, result2, result3, result4, result5):
	"""Simply multiply the final results"""
	final_result = result1 * result2 * result3 * result4 * result5

	return final_result

file = "day_3_input.txt"
file2 = "day_3_input - Copy.txt"

lines = _list_from_file(file2)
result1 = count_trees(lines, 3) 
print(f"The total number of trees is {result1}.")


"""--- Part Two ---
Time to check the rest of the slopes - you need to minimize the probability
of a sudden arboreal stop, after all.

Determine the number of trees you would encounter if, for each of
the following slopes, you start at the top-left corner and traverse
the map all the way to the bottom:

Right 1, down 1.
Right 3, down 1. (This is the slope you already checked.)
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.
In the above example, these slopes would find 2, 7, 3, 4,
and 2 tree(s) respectively; multiplied together, these produce the answer 336.

What do you get if you multiply together
the number of trees encountered on each of the listed slopes?"""

result2 = count_trees(lines, 1) 
print(f"The total number of trees is {result2}.")

result3 = count_trees(lines, 5) 
print(f"The total number of trees is {result3}.")

result4 = count_trees(lines, 7) 
print(f"The total number of trees is {result4}.")

result5 = count_trees(lines, 1, 2) 
print(f"The total number of trees is {result5}.")

final_result = multiply_results(result1, result2, result3, result4, result5)
print(f"The final result is {final_result}.")