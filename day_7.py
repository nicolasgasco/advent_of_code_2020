"""--- Day 7: Handy Haversacks ---
You land at the regional airport in time for your next flight.
In fact, it looks like you'll even have time to grab some food:
all flights are currently delayed due to issues in luggage processing.

Due to recent aviation regulations, many rules (your puzzle input) are being
enforced about bags and their contents; bags must be color-coded and
must contain specific quantities of other color-coded bags. Apparently,
nobody responsible for these regulations considered how long they would take
to enforce!

For example, consider the following rules:

light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.

These rules specify the required contents for 9 bag types. In this example,
every faded blue bag is empty, every vibrant plum bag contains 11 bags
(5 faded blue and 6 dotted black), and so on.

You have a shiny gold bag. If you wanted to carry it in at least one other bag,
how many different bag colors would be valid for the outermost bag?
(In other words: how many colors can, eventually, contain at least one
shiny gold bag?)

In the above rules, the following options would be available to you:

A bright white bag, which can hold your shiny gold bag directly.
A muted yellow bag, which can hold your shiny gold bag directly,
plus some other bags.
A dark orange bag, which can hold bright white and muted yellow bags,
either of which could then hold your shiny gold bag.
A light red bag, which can hold bright white and muted yellow bags,
either of which could then hold your shiny gold bag.
So, in this example, the number of bag colors that can eventually contain
at least one shiny gold bag is 4.

How many bag colors can eventually contain at least one shiny gold bag?
(The list of rules is quite long; make sure you get all of it.)

To begin, get your puzzle input.

--- Part Two ---
It's getting pretty expensive to fly these days - not because of ticket prices,
but because of the ridiculous number of bags you need to buy!

Consider again your shiny gold bag and the rules from the above example:

faded blue bags contain 0 other bags.
dotted black bags contain 0 other bags.
vibrant plum bags contain 11 other bags: 5 faded blue bags and 6 dotted black bags.
dark olive bags contain 7 other bags: 3 faded blue bags and 4 dotted black bags.

So, a single shiny gold bag must contain 1 dark olive bag
(and the 7 bags within it) plus 2 vibrant plum bags (and the 11 bags within each
 of those): 1 + 1*7 + 2 + 2*11 = 32 bags!

Of course, the actual rules have a small chance of going several levels deeper
than this example; be sure to count all of the bags, even if the nesting
becomes topologically impractical!

Here's another example:

shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.

In this example, a single shiny gold bag must contain 126 other bags.

How many individual bags are required inside your single shiny gold bag?

--- Part Two ---
It's getting pretty expensive to fly these days - not because of ticket prices, but because of the ridiculous number of bags you need to buy!

Consider again your shiny gold bag and the rules from the above example:

faded blue bags contain 0 other bags.
dotted black bags contain 0 other bags.
vibrant plum bags contain 11 other bags: 5 faded blue bags and 6 dotted black bags.
dark olive bags contain 7 other bags: 3 faded blue bags and 4 dotted black bags.
So, a single shiny gold bag must contain 1 dark olive bag (and the 7 bags within it) plus 2 vibrant plum bags (and the 11 bags within each of those): 1 + 1*7 + 2 + 2*11 = 32 bags!

Of course, the actual rules have a small chance of going several levels deeper than this example; be sure to count all of the bags, even if the nesting becomes topologically impractical!

Here's another example:

shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
In this example, a single shiny gold bag must contain 126 other bags.

How many individual bags are required inside your single shiny gold bag?"""

import re

file = "day_7.txt"

# pattern1 = re.compile(r"(\w+\s\w+) bags contain( [\,]?\d+ \w+\s\w+ bag[s]?[,]?)+\.")
# #This one is necessary two fully capture the second group
# pattern2 = re.compile(r"(\w+\s\w+) bags contain no other bags.")
# pattern3 = re.compile(r"(\d+) (\w+\s\w+) bag[s]?")



# with open(file) as f:
# 	lines = f.readlines()

# # List of dictionaries with all the rules
# list_all_rules = []
# for line in lines:
# 	# Every rule will be an item of this dict
# 	dict_single_rule = {}

# 	match1 = re.fullmatch(pattern1, line.rstrip())
# 	match2 = re.fullmatch(pattern2, line.rstrip())
# 	match3 = re.findall(pattern3, line.rstrip())

# 	if match2:
		
# 		dict_single_rule["main_bag"] = match2.group(1)

# 		# Dictionary required because of consistency
# 		dict_single_rule["bags_inside_main"] = []
# 		contained_bag = {}
# 		contained_bag["contained_bag"] = None
# 		contained_bag["number_contained"] = 0

# 		# Every single bag is a dict, up to 3-4 in a single rule
# 		dict_single_rule["bags_inside_main"].append(contained_bag)

# 		# One rule at a time for every rule
# 		list_all_rules.append(dict_single_rule)

# 	# These are potential good matches
# 	if match1:
		
# 		# Extract the color of main bag
# 		dict_single_rule["main_bag"] = match1.group(1)

# 		# The bags contained in the main one will be a list of dicts
# 		dict_single_rule["bags_inside_main"] = []
# 		for match in match3:
# 			contained_bag = {}
# 			contained_bag["contained_bag"] = match[1]
# 			contained_bag["number_contained"] = match[0]

# 			# Every single bag is a dict, up to 3-4 in a single rule
# 			dict_single_rule["bags_inside_main"].append(contained_bag)
		
# 		# One rule at a time for every rule
# 		list_all_rules.append(dict_single_rule)

# bag_colors = []

# # These are the ones that hold directly a shiny golden one
# for dictionary in list_all_rules:
# 	for bag in dictionary["bags_inside_main"]:
# 		if bag["contained_bag"] == "shiny gold":
# 			bag_colors.append(dictionary["main_bag"])




# # Now the bags that hold another bag able to hold "shiny golden"
# for color in bag_colors:
# 	for dictionary in list_all_rules:
# 		# For every bag in the bags inside main (1-4)
# 		for bag in dictionary["bags_inside_main"]:
# 			if bag["contained_bag"] != None and color in bag["contained_bag"]:
# 				bag_colors.append(dictionary["main_bag"])



# print(f"The solution is {len(set(bag_colors))}.")



# desidered_main_bag = "shiny gold"

# number_of_bags = 0

# desidered_dictionaries = ["shiny gold"]
# while len(desidered_dictionaries) != 0: 
# 		for desidered_dictionary in desidered_dictionaries:
# 			print(f"1) This is the dictionary desired: {desidered_dictionary}")
# 			desidered_dictionaries.remove(desidered_dictionary)
# 			for dictionary in list_all_rules:
# 				if dictionary["main_bag"] == desidered_dictionary:
# 					print(f"2) Dicitionary was found: {dictionary}.")

# 					for bag in dictionary["bags_inside_main"]:
						
# 						if bag['number_contained'] == 0:
# 							print(f"3) Bag {bag['contained_bag']} is empty!")

# 						else:
# 							number_of_bags += int(bag['number_contained'])

# 							print(f"3) Current bag is {bag['contained_bag']}.")
# 							desidered_dictionaries.append(bag["contained_bag"])
# 							print(f"Desired dictionaries is {desidered_dictionaries}")


# print(number_of_bags)




# bag_count = 0
# multiplier = 1
# while desidered_main_bag != None:
# 	for dictionary in list_all_rules:
# 		while dictionary["main_bag"] == desidered_main_bag:
# 			print(dictionary, "Here we find the starting dictionary with other bags\n\n\n")

# 			bags_name = []
# 			for bag in dictionary["bags_inside_main"]:
# 				desidered_main_bag = bag["contained_bag"]
# 				print(f"desidered_main_bag is {desidered_main_bag}")

# 				print(f"Multiplier is {multiplier} at start")
# 				print(f"The number of bags is {int(bag['number_contained'])}")

			
# 				num_bags = int(bag["number_contained"])
# 				bag_count += num_bags * multiplier
# 				multiplier = int(bag["number_contained"])

# 				print(f"Bag count is now {bag_count}")
# 				print(f"Multiplier is now {multiplier}")
				

# 				contained_bag_name = bag["contained_bag"]
# 				print(f"We found {num_bags} '{contained_bag_name}' bag")
# 				print("\n\n\n_____________________________")

# 				bags_name.append(contained_bag_name)

# 		else:
# 			print("This dictionary doesn't contain other dictionaries")

# else:
# 	print(f"Does {bag['contained_bag']} has 0 bags for real??")

					
# print(bag_count)

with open(file) as f:
	lines = f.readlines()
	lines = [line.rstrip() for line in lines]




# 2 muted aqua, 3 bright salmon bag, 4 striped violet, 2 posh brown

def get_bag_count(color):
	rule = ""
	for line in lines:
		if line[:line.index(" bags")] == color:
			rule = line

	if "no" in rule:
		return 1

	
	rule = rule[rule.index("cont")+8:].split()

	total = 0
	i = 0
	while i < len(rule):
		count = int(rule[i])
		colour = rule[i+1] + " " + rule[i+2]

		total += count * int(get_bag_count(colour)) 

		i += 4

	return total +1 


result = get_bag_count("shiny gold")
print(result -1)