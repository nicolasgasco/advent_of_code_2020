"""--- Day 14: Docking Data ---
As your ferry approaches the sea port, the captain asks for your help again.
The computer system that runs this port isn't compatible with the docking
program on the ferry, so the docking parameters aren't being correctly
initialized in the docking program's memory.

After a brief inspection, you discover that the sea port's computer system uses
a strange bitmask system in its initialization program. Although you don't have
the correct decoder chip handy, you can emulate it in software!

The initialization program (your puzzle input) can either update the bitmask
or write a value to memory. Values and memory addresses are both 36-bit
unsigned integers. For example, ignoring bitmasks for a moment, a line like
mem[8] = 11 would write the value 11 to memory address 8.

The bitmask is always given as a string of 36 bits, written with the most
significant bit (representing 2^35) on the left and the least significant bit
(2^0, that is, the 1s bit) on the right. The current bitmask is applied to
values immediately before they are written to memory: a 0 or 1 overwrites the
corresponding bit in the value, while an X leaves the bit in the value unchanged.

For example, consider the following program:

mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0
This program starts by specifying a bitmask (mask = ....). The mask it specifies
will overwrite two bits in every written value: the 2s bit is overwritten with 0,
and the 64s bit is overwritten with 1.

The program then attempts to write the value 11 to memory address 8. By expanding
everything out to individual bits, the mask is applied as follows:

value:  000000000000000000000000000000001011  (decimal 11)
mask:   XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
result: 000000000000000000000000000001001001  (decimal 73)
So, because of the mask, the value 73 is written to memory address 8 instead.
Then, the program tries to write 101 to address 7:

value:  000000000000000000000000000001100101  (decimal 101)
mask:   XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
result: 000000000000000000000000000001100101  (decimal 101)
This time, the mask has no effect, as the bits it overwrote were already the
values the mask tried to set. Finally, the program tries to write 0 to address 8:

value:  000000000000000000000000000000000000  (decimal 0)
mask:   XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
result: 000000000000000000000000000001000000  (decimal 64)
64 is written to address 8 instead, overwriting the value that was there
previously.

To initialize your ferry's docking program, you need the sum of all values
left in memory after the initialization program completes. (The entire 36-bit
address space begins initialized to the value 0 at every address.) In the above
example, only two values in memory are not zero - 101 (at address 7) and 64
(at address 8) - producing a sum of 165.

Execute the initialization program. What is the sum of all values left in memory
after it completes?

To begin, get your puzzle input.

__Part 2__

For some reason, the sea port's computer system still can't communicate with your
ferry's docking program. It must be using version 2 of the decoder chip!

A version 2 decoder chip doesn't modify the values being written at all. Instead,
it acts as a memory address decoder. Immediately before a value is written to
memory, each bit in the bitmask modifies the corresponding bit of the
destination memory address in the following way:

If the bitmask bit is 0, the corresponding memory address bit is unchanged.
If the bitmask bit is 1, the corresponding memory address bit is overwritten
with 1.
If the bitmask bit is X, the corresponding memory address bit is floating.
A floating bit is not connected to anything and instead fluctuates unpredictably.
In practice, this means the floating bits will take on all possible values,
potentially causing many memory addresses to be written all at once!

For example, consider the following program:

mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1
When this program goes to write to memory address 42, it first applies the
bitmask:

address: 000000000000000000000000000000101010  (decimal 42)
mask:    000000000000000000000000000000X1001X
result:  000000000000000000000000000000X1101X
After applying the mask, four bits are overwritten, three of which are different,
and two of which are floating. Floating bits take on every possible combination
of values; with two floating bits, four actual memory addresses are written:

000000000000000000000000000000011010  (decimal 26)
000000000000000000000000000000011011  (decimal 27)
000000000000000000000000000000111010  (decimal 58)
000000000000000000000000000000111011  (decimal 59)
Next, the program is about to write to memory address 26 with a different bitmask:

address: 000000000000000000000000000000011010  (decimal 26)
mask:    00000000000000000000000000000000X0XX
result:  00000000000000000000000000000001X0XX
This results in an address with three floating bits, causing writes to eight
memory addresses:

000000000000000000000000000000010000  (decimal 16)
000000000000000000000000000000010001  (decimal 17)
000000000000000000000000000000010010  (decimal 18)
000000000000000000000000000000010011  (decimal 19)
000000000000000000000000000000011000  (decimal 24)
000000000000000000000000000000011001  (decimal 25)
000000000000000000000000000000011010  (decimal 26)
000000000000000000000000000000011011  (decimal 27)
The entire 36-bit address space still begins initialized to the value 0 at every
address, and you still need the sum of all values left in memory at the end of
the program. In this example, the sum is 208.

Execute the initialization program using an emulator for a version 2 decoder
chip. What is the sum of all values left in memory after it completes?"""

file = "day_14_input.txt"

with open(file) as f:
	data = f.readlines()
	data = [line.rstrip() for line in data]

# mem_locations = [line.split()[0] for line in data if line.startswith("mem")]


def reverse_number(num):
	"""Function to write a number in reverse: 123 -> 321"""
	new_num = ""
	for i in range(1, len(str(num))+1):
		new_num += num[-i]

	return new_num

# Empty dictionary with all unique locations
mem_locations = {}

for line in data:
	
	# if line with mask pattern
	if line[:4] == "mask":
		# Just the pattern
		mask_string = line[7:]

	# Line with command
	else:
		# This is the original decimal to write in memory
		number_to_write = int(line[line.index("=")+2:])
		number_binary = str("{0:b}".format(number_to_write))

		# Create new number from the end, will be reversed
		new_number_reversed = ""
		
		i = -1
		while i >= -(len(mask_string)):

			# If X, then leave original number or 0
			if mask_string[i] == "X":

				# it can also be out of range
				try:
					new_number_reversed += number_binary[i]
				except:
					# If out of range than it's 0
					new_number_reversed += str(0)
				i -= 1

			else:
				# The number from the mask pattern
				new_number_reversed += mask_string[i]

				i -= 1
		
		# Binary number must be reversed
		new_number = reverse_number(new_number_reversed)

		# Transform it to decimal
		decimal_number = int(new_number, 2)

		# Add to dictionary, repeated values will be updated
		mem_locations[line[:line.index("]")+1]] = decimal_number


# Sum of all values
result = sum(mem_locations.values())

print(f"The result of the first part is {result}.")

# Part 2

# Mask is for memory location, number in squared brackets is value to modify
import itertools
file = "day_14_input.txt"

with open(file) as f:
	data = f.readlines()
	data = [line.rstrip() for line in data]

# Dictionary where all locations will be
memory_locations = {}

for command in data:
	if command[:4] == "mask":
		mask = command[7:]
	
	else:
		# Memory position
		memory_value = int(command[4:command.index("]")])
		memory_value_binary = "{0:b}".format(memory_value)

		# Value to be written in memory
		value_to_be_written = int(command[command.index("=")+2:])

		# Reversed because we'll read mask from -1 on
		new_memory_value_reversed = ""

		i = -1
		# Because mask and value don't have the same lenght
		while i >= -(len(mask)):

			# If X, then X
			if mask[i] == "X":
				new_memory_value_reversed += "X"
				i -= 1

			# If 1 then 1
			elif mask[i] == "1":
				new_memory_value_reversed += "1"
				i -= 1

			# If 0 then keep the same number from value
			elif mask[i] == "0":

				# It might be out of index
				try:
					new_memory_value_reversed += memory_value_binary[i]
					i -= 1

				except:
					new_memory_value_reversed += "0"
					i -= 1
		
		# Binary number must be reversed
		new_memory_value = reverse_number(new_memory_value_reversed)

		X = [0,1]

		#Bad design, a big number to cover all cases
		combinations_X = list(itertools.product(X, X, X, X, X, X, X, X, X, X))

		# To gather all possible memory locations
		memory_locations_after_mask = []

		# One combination for each in combinations_X
		for number_items in combinations_X:
			new_memory_value_string = ""

			# This is to catch all positions in the itertools
			i = 0

			
			for character in new_memory_value:
				# X can be either 1 or 0
				if character == "X":
					new_memory_value_string += str(number_items[i])
					i += 1

				# Number doesn't change
				else:
					new_memory_value_string += character
			
			memory_locations_after_mask.append(new_memory_value_string)

		for memory_location in memory_locations_after_mask:
			# Change memory_location to integer
			memory_locations[int(memory_location, 2)] = value_to_be_written

result = sum(memory_locations.values())
print(f"The result of the second part is {result}.")

