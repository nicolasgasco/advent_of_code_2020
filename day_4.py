import json
import re

"""--- Day 4: Passport Processing ---
You arrive at the airport only to realize that you grabbed your North Pole
Credentials instead of your passport. While these documents are extremely similar,
North Pole Credentials aren't issued by a country and therefore aren't actually
valid documentation for travel in most of the world.

It seems like you're not the only one having problems, though; a very long line
has formed for the automatic passport scanners, and the delay could upset your
travel itinerary.

Due to some questionable network security, you realize you might be able to
solve both of these problems at the same time.

The automatic passport scanners are slow because they're having trouble
detecting which passports have all required fields. The expected fields are as follows:

byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
Passport data is validated in batch files (your puzzle input). Each passport
is represented as a sequence of key:value pairs separated by spaces or newlines.
Passports are separated by blank lines.

Here is an example batch file containing four passports:

ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in

The first passport is valid - all eight fields are present. The second passport
is invalid - it is missing hgt (the Height field).

The third passport is interesting; the only missing field is cid, so it looks
like data from North Pole Credentials, not a passport at all! Surely, nobody
would mind if you made the system temporarily ignore missing cid fields.
Treat this "passport" as valid.

The fourth passport is missing two fields, cid and byr.
Missing cid is fine, but missing any other field is not,
so this passport is invalid.

According to the above rules, your improved system would report 2 valid passports.

Count the number of valid passports - those that have all required fields.
Treat cid as optional. In your batch file, how many passports are valid?"""

def _string_from_file(file):
	"""Create one big string from a file"""
	with open(file) as f:
		lines = f.read()
	return lines


def _extract_data_from_list(string):
	"""Given the input as a string, extract all the chunks separated by \n\n"""
	# Using regex groups here
	pattern = re.compile(r"\n\n")	
	new_list = re.split(pattern, string)

	# This is to remove \n inside one passport
	final_list = []
	for el in new_list:
		x = el.replace("\n", " ")
		final_list.append(x)

	return final_list


def _create_dictionary_from_list(lst):
	"""Create a dictionary of key:value pairs from a single string"""
	new_list = []

	for string in lst:
		new_dict = {}
		# Using regex groups to extract the key and the value
		pattern = re.compile(r"(\w{3}):([#]?\w*)")	
		matches = re.finditer(pattern, string)
		
		for match in matches:
			new_dict[match.group(1)] = match.group(2)
		new_list.append(new_dict)

	return new_list


def file_to_dictionary(file):
	"""From a file of raw text, create a collection of dictionaries
	with key:value pairs"""
	
	new_string = _string_from_file(file)
	new_list = _extract_data_from_list(new_string)
	new_dict = _create_dictionary_from_list(new_list)

	return new_dict


"""The line is moving more quickly now, but you overhear airport security
talking about how passports with invalid data are getting through. Better add
some data validation, quick!

You can continue to ignore the cid field, but each other field has strict rules
about what values are valid for automatic validation:

byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
Your job is to count the passports where all required fields are both present
and valid according to the above rules. Here are some example values:

byr valid:   2002
byr invalid: 2003

hgt valid:   60in
hgt valid:   190cm
hgt invalid: 190in
hgt invalid: 190

hcl valid:   #123abc
hcl invalid: #123abz
hcl invalid: 123abc

ecl valid:   brn
ecl invalid: wat

pid valid:   000000001
pid invalid: 0123456789

Here are some invalid passports:

eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007
Here are some valid passports:

pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719

Count the number of valid passports - those that have all required fields
and valid values. Continue to treat cid as optional. In your batch file,
how many passports are valid?"""


def filter_valid_first_round(lst):
	"""Remove all entries which are not valid as per first definition
	(Only keep passports with 8 values of 7 if CID is missing)"""
	new_list = []
	for dict in lst:
		# The two options cannot be joined because passport with 8 values
		# always contains CID
		if len(dict) == 8:
			new_list.append(dict)
		elif len(dict) == 7 and "cid" not in dict.keys():
			new_list.append(dict)
	
	return new_list


def is_byr_valid(dict):
	"""Check if byr is valid. Conditions: four digits; at least 1920 and at most 2002"""
	
	if "byr" in dict:
		byr = dict["byr"]
		pattern = re.compile(r"\d{4}")
		# Fullmatch necessary to avoid false positives
		if re.fullmatch(pattern, byr): 
			if 1920 <= int(byr) <= 2002:
				return True
			else:
				return False
		else:
			return False
	else:
		return False


def is_eyr_valid(dict):
	"""Check if eyr is valid. Conditions: four digits; at least 2020 and at most 2030"""
	
	if "eyr" in dict:
		eyr = dict["eyr"]
		pattern = re.compile(r"\d{4}")
		if re.fullmatch(pattern, eyr):
			if 2020 <= int(eyr) <= 2030:
				return True
			else:
				return False
		else:
			return False
	else:
		return False


def is_iyr_valid(dictionary):
	"""Check if iyr is valid. Conditions: four digits; at least 2010 and at most 2020"""
	
	if "iyr" in dictionary:
		iyr = dictionary["iyr"]
		pattern = re.compile(r"\d{4}")
		if re.fullmatch(pattern, iyr):
			if 2010 <= int(iyr) <= 2020:
				return True
			else:
				return False
		else:
			return False
	else:
		return False


def is_hgt_valid(dict):
	"""Check if hgt is valid. Conditions: a number followed by either cm or in
	If cm, the number must be at least 150 and at most 193.
	If in, the number must be at least 59 and at most 76."""
	
	if "hgt" in dict:
		hgt = dict["hgt"]
		pattern = re.compile(r"(\d*)(cm|in)")
		# This was necessary because there were some values with invalid heigth
		if re.fullmatch(pattern, hgt):
			match = re.fullmatch(pattern, hgt)
			value = match.group(1)
			unit = match.group(2)
			if unit == "cm":
				if 150 <= int(value) <= 193:
					return True
				else:
					return False
			elif unit == "in":
				if 59 <= int(value) <= 76:
					return True
				else:
					return False
			else:
				return False
		else:
			return False
	else:
		return False


def is_hcl_valid(dictionary):
	"""Check if hcl is valid. Conditions: # followed by exactly six characters 0-9 or a-f"""
	
	if "hcl" in dictionary:
		string = dictionary["hcl"]
		pattern = re.compile(r"#[0-9a-f]{6}")
		if re.fullmatch(pattern, string):
			return True
		else:
			return False
	else:
		return False

def is_ecl_valid(dict):
	"""Check if ecl is valid. Conditions: exactly one of: amb blu brn gry grn hzl oth"""
	
	if "ecl" in dict:
		string = dict["ecl"]
		colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
		if string in colors:
			return True
		else:
			return False
	else:
		return False


def is_pid_valid(dict):
	"""Check if pid is valid. Conditions: a nine-digit number, including leading zeroes"""
	
	if "pid" in dict:
		string = dict["pid"]
		pattern = re.compile(r"\d{9}")
		if re.fullmatch(pattern, string):
			return True
		else:
			return False
	else:
		return False


def count_valid(lst):
	"""Check if all values of passports are valid except for CID"""
	valid_count = 0
	for dict in lst:
		eyr = is_eyr_valid(dict)
		hcl = is_hcl_valid(dict)
		ecl = is_ecl_valid(dict)
		hgt = is_hgt_valid(dict)
		pid = is_pid_valid(dict)
		iyr = is_iyr_valid(dict)
		byr = is_byr_valid(dict)

		if eyr and hcl and ecl and hgt and pid and iyr and byr:
		  	valid_count += 1
		else:
		 	pass

	return valid_count


file = "day_4_input.txt"
file2 = "day_4_input2.txt"


passport_dictionary = file_to_dictionary(file)

# This returns the number of valid passports as per first selection
passports_filtered_first = filter_valid_first_round(passport_dictionary)


total_valid = count_valid(passports_filtered_first)
print(f"The total numer of valid passports is {total_valid}.")


# Keeping this for history
# def filter_valid_second_round(lst):
# 	"""Remove all entries which don't contain all keys"""
# 	new_list = []
# 	values = ["eyr", "hgt", "iyr", "hcl", "ecl", "byr", "pid"]
# 	for dict in lst:
# 		value_count = 0
# 		for value in values:
# 			if value in dict.keys():
# 				value_count += 1
# 		if value_count == 7:
# 			new_list.append(dict)

# 	return new_list