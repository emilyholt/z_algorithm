'''
Generate a 'needle(s) in a haystack' file to test z-algorithm
'''

import random
from tqdm import tqdm

output_file = "needle_in_a_haystack.txt"

indices = []

file_size = 2000000
for i in range(0,5):
	n = random.randint(1,file_size)
	indices.append(n)

for i in tqdm(range(file_size)):
	if i in indices:
		with open(output_file, 'a') as f:
			f.write('needle')
	else:
		with open(output_file, 'a') as f:
			f.write('haystack')