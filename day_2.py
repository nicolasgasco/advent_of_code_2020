import re

"""Your flight departs in a few days from the coastal airport; the easiest way
 down to the coast from here is via toboggan.

The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day.
"Something's wrong with our computers; we can't log in!" You ask ifyou can take a look.

Their password database seems to be a little corrupted: some of the passwords
wouldn't have been allowed by the Official Toboggan Corporate Policy
that was in effect when they were chosen.

To try to debug the problem, they have created a list (your puzzle input)
of passwords (according to the corrupted database) and the corporate policy
when that password was set.

For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
Each line gives the password policy and then the password. The password policy
indicates the lowest and highest number of times a given letter must appear
for the password to be valid. For example, 1-3 a means that the password
must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg,
is not; it contains no instances of b, but needs at least 1.
The first and third passwords are valid: they contain one a or nine c,
both within the limits of their respective policies.

How many passwords are valid according to their policies?"""

def _list_from_file(file):
	"""Create a list from a file"""
	with open(file) as f:
		new_list = []
		passwords = f.readlines()
	for password in passwords:
		new_list.append(password.rstrip())
	return new_list



def _extract_data_from_list(lst):
	new_list = []
	"""Given the input as list, extract all the relevant data as single variables"""
	for el in lst:
		new_dict = {}
		pattern = re.compile(r"(\d+)-(\d+) (\w): (\w+)")	
		for match in re.finditer(pattern, el):
			new_dict["num1"] = int(match.group(1))
			new_dict["num2"] = int(match.group(2))
			new_dict["letter"] = match.group(3)
			new_dict["password"] = match.group(4)
			new_list.append(new_dict)

	return new_list



def count_valid_first_policy(lst):
	"""Count the ocurrences of valid passwords from a list of dictionaries"""
	total_valid = 0
	for el in lst:
		password = el["password"]
		letter = el["letter"]
		num1 = el["num1"]
		num2 = el["num2"]
		ocurrences = password.count(letter)
		if num1 <= ocurrences <= num2:
			total_valid += 1

	return total_valid


"""While it appears you validated the passwords correctly, they don't seem
to be what the Official Toboggan Corporate Authentication System is expecting.

The shopkeeper suddenly realizes that he just accidentally explained
the password policy rules from his old job at the sled rental place down the street!
The Official Toboggan Corporate Policy actually works a little differently.

Each policy actually describes two positions in the password,
where 1 means the first character, 2 means the second character, and so on.
(Be careful; Toboggan Corporate Policies have no concept of "index zero"!)
Exactly one of these positions must contain the given letter.
Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

Given the same example list from above:

1-3 a: abcde is valid: position 1 contains a and position 3 does not.
1-3 b: cdefg is invalid: neither position 1 nor position 3 contains b.
2-9 c: ccccccccc is invalid: both position 2 and position 9 contain c.
How many passwords are valid according
to the new interpretation of the policies?"""

def count_valid_second_policy(lst):
	"""Count the ocurrences of valid passwords from a list of dictionaries"""
	total_valid = 0
	for el in lst:
		password = el["password"]
		letter = el["letter"]
		num1 = el["num1"]
		num2 = el["num2"]
		if password[num1 -1] == letter and password[num2 -1] != letter:
			total_valid += 1
		elif password[num1 -1] != letter and password[num2 -1] == letter:
			total_valid += 1

	return total_valid


file = "day_2_input.txt"
my_input = _list_from_file(file)
password_list = _extract_data_from_list(my_input)

result1 = count_valid_first_policy(password_list)
print(f"The total number of valid passwords is: {result1}.")

result2 = count_valid_second_policy(password_list)
print(f"The total number of valid passwords is: {result2}.")