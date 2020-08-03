import argparse
from z_algo import *

def naive(pattern, input_string):
    # z_input = "AABAABCAXAABAABCYAAAAB"
    z_input = pattern + "$" + input_string
    z_box = find_z_box(z_input)
    right_endpoints = find_right_endpoints(z_input, z_box)
    left_endpoints = find_left_endpoints(z_input, z_box, right_endpoints)
    z_box[0] = 0

    # Formatting for printing
    test_string = [str(x) + " " for x in z_input]
    z_box = [str(x) + " " if x < 10 else str(x) for x in z_box]
    right_endpoints = [str(x) + " " if x < 10 else str(x) for x in right_endpoints]
    left_endpoints = [str(x) + " " if x < 10 else str(x) for x in left_endpoints]
    
    print(f"\n################################################")
    print(f"\n\tResults\n........................\n")
    print(f"Test string:                {test_string}")
    print(f"Resulting z-box:            {z_box}")
    print(f"Resulting right_endpoints:  {right_endpoints}")
    print(f"Resulting left_endpoints:   {left_endpoints}")

def advanced(pattern, input_string):
    z_input = pattern + "$" + input_string
    # z_input = "AABAABCAXAABAABCYAAAAB"
    z_box = z_algo(z_input)

    # Formatting for printing
    indices = [str(x) + " " if x < 10 else str(x) for x in range(len(z_input))]
    test_string = [str(x) + " " for x in z_input]
    z_box = [str(x) + " " if x < 10 else str(x) for x in z_box]
    
    print(f"\n################################################")
    print(f"\n\tResults\n........................\n")
    print(f"Indices:            {indices}")
    print(f"Test string:        {test_string}")
    print(f"Resulting z-box:    {z_box}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("pattern", help="pattern to search for")
    parser.add_argument("input_string", help="pattern to search for")
    args = parser.parse_args()
    advanced(args.pattern, args.input_string)