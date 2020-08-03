import operator

def longest_common_substring(input_string, z_box):

	index, value = max(enumerate(z_box), key=operator.itemgetter(1))
	stop = index + int(value)

	print(f"Longest Common substring found at index [{index}] = {value}")
	print(f"Substring = {input_string[index:stop]}")