'''
Generate a 'needle(s) in a haystack' file to test z-algorithm
'''
import argparse
import os
import random

from tqdm import tqdm

from experiments import run_comparison

output_file = "needle_in_a_haystack.txt"

def file_test():
    test_file = 'needle_in_a_haystack.txt'
    file_size = os.stat(test_file).st_size
    print(f"Test file size: {file_size}")
    with open(test_file, 'r') as f:
        data = f.read().replace('\n', '')
    run_comparison("needle", data)

def generate_test_file(file_size):
    indices = []

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

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("file_size", help="approx size of file to generate")
    args = parser.parse_args()
    generate_test_file(int(args.file_size))
    file_test()