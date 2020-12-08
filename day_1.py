"""--- Day 1: Report Repair ---
After saving Christmas five years in a row, you've decided to take a vacation at
a nice resort on a tropical island. Surely, Christmas will go on without you.

The tropical island has its own currency and is entirely cash-only.
The gold coins used there have a little picture of a starfish; the locals just
call them stars. None of the currency exchanges seem to have heard of them,
but somehow, you'll need to find fifty of these coins by the time you arrive
so you can pay the deposit on your room.

To save your vacation, you need to get all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day
in the Advent calendar; the second puzzle is unlocked when you complete the
first. Each puzzle grants one star. Good luck!

Before you leave, the Elves in accounting just need you to fix your expense
report (your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to find the two entries that sum to 2020
and then multiply those two numbers together.

For example, suppose your expense report contained the following:

1721
979
366
299
675
1456
In this list, the two entries that sum to 2020 are 1721 and 299.
Multiplying them together produces 1721 * 299 = 514579, so the correct answer
is 514579.

Of course, your expense report is much larger. Find the two entries
that sum to 2020; what do you get if you multiply them together?"""


def list_from_file(file):
	"""Create a list from a file"""
	with open(file) as f:
		new_list = []
		nums = f.readlines()

	for num in nums:
		new_list.append(int(num.rstrip()))

	return new_list


def find_two_to_2020(lst):
	"""Finds two numbers in a list whose sum is 2020 and multiplies them"""
	results = []
	for el in lst:
		for i in range(len(lst)):
			# We don't want to sum the number by itself
			if el != lst[i]:
				if el + lst[i] == 2020:
					results.append(lst[i])

	return results


def find_two_to_2020_optimized(lst):
	"""Finds two numbers in a list whose sum is 2020 and multiplies them, optimized"""
	results = []
	for el in lst:
		difference = 2020 - el
		if difference in lst:
			results.append(difference)

	return results

my_input = list_from_file("day_1_input.txt")
results = find_two_to_2020_optimized(my_input)

print(f"The two numbers are: {results[0]} and {results[1]}.")
print(f"The solution is: {results[0] * results [1]}.")


"""The Elves in accounting are thankful for your help; one of them even offers
you a starfish coin they had left over from a past vacation. They offer you
a second one if you can find three numbers in your expense report that meet
the same criteria.

Using the above example again, the three entries that sum to 2020 are 979, 366,
and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?"""

def find_three_to_2020(lst):
	"""Finds three numbers in a list whose sum is 2020 and multiplies them"""
	results = set()
	for el in lst:
		for i in range(len(lst)):
		# We rule out sum of the same number and sums which are already > 2020
			if el != lst[-i] and (el + lst[i]) < 2020:
				sum = el + lst[i]
				for c in range(len(lst)):
				# We don't sum the same numbers
					if lst[c] != el and c != lst[i]:
						if sum + lst[c] == 2020:
							results.add(el)
	
	return list(results)


solution2 = find_three_to_2020(my_input)

print(f"The three numbers are: {solution2[0]}, {solution2[1]}, {solution2[2]}.")
print(f"The solution is: {solution2[0] * solution2[1] * solution2[2]}.")

