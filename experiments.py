import argparse
import os
import time

from z_algo import *
from comparisons.boyer_moore_algo import bm

def naive(pattern, input_string):
    z_input = pattern + "$" + input_string
    z_box = find_z_box(z_input)
    z_box[0] = 0

def advanced(pattern, input_string):
    z_input = pattern + "$" + input_string
    z_box = z_algo_streamlined(z_input, descriptive=False)

def run_comparison(pattern, input_string):

    naive_start = time.time()
    naive(pattern, input_string)
    naive_end = time.time()
    print(f"Naive z-box computation took: {naive_end - naive_start}")

    advanced_start = time.time()
    advanced(pattern, input_string)
    advanced_end = time.time()
    print(f"Advanced z-box computation took: {advanced_end - advanced_start}")

    bm_start = time.time()
    bm(pattern, input_string)
    bm_end = time.time()
    print(f"Boyer-Moore pattern-match computation took: {bm_end - bm_start}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("pattern", help="pattern to search for")
    parser.add_argument("input_string", help="pattern to search for")
    args = parser.parse_args()
    run_comparison(args.pattern, args.input_string)
