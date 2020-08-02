import argparse
from colorama import init, Fore, Back, Style

init()

def pretty_print_zbox(input_string, pattern_index, current_index):
    pattern_string = ""
    intermediate_string = ""
    z_string = ""
    end_string = ""

    # Separate the pattern & z-boxes into strings
    for i, elem in enumerate(input_string):
        if i <= pattern_index:
            pattern_string = pattern_string + str(elem) + " "
        elif i < current_index:
            intermediate_string = intermediate_string + str(elem) + " "
        elif i <= current_index + pattern_index:
            z_string = z_string + str(elem) + " "
        else:
            end_string = end_string + str(elem) + " "

    # Pretty printing of our color-coded z-box
    print(Fore.GREEN + pattern_string
        + Fore.RESET + intermediate_string
        + Fore.BLUE + z_string
        + Fore.RESET + end_string
        , end='\n')

def find_z_box(input_string, descriptive=True):
    z_box = [0] * len(input_string)
    
    left_endpoints = [0] * len(input_string)
    
    for current_index in range(1, len(input_string)):
        pattern_index = 0
        while pattern_index + current_index < len(input_string)\
         and input_string[pattern_index] == input_string[pattern_index + current_index]:
            
            if descriptive:
                print(f"\nCurrent Index: {current_index}")
                print(f"Found new match: input[{current_index + pattern_index}] = {input_string[current_index + pattern_index]} = input[{pattern_index}] = {input_string[pattern_index]}")
                pretty_print_zbox(input_string, pattern_index, current_index)

            pattern_index += 1

        z_box[current_index] = pattern_index
    return z_box

def find_right_endpoints(input_string, z_box):
    right_endpoints = [0] * len(input_string)
    rightmost_endpoint = 0

    for current_index in range(1, len(input_string)):
        if z_box[current_index] is not 0:
            candidate_endpoint = current_index + z_box[current_index]
            
            if candidate_endpoint > rightmost_endpoint:
                rightmost_endpoint = candidate_endpoint - 1

        right_endpoints[current_index] = rightmost_endpoint

    return right_endpoints

def find_left_endpoints(input_string, z_box, right_endpoints):
    left_endpoints = [0] * len(input_string)
    leftmost_endpoint = 0

    for current_index in range(1, len(input_string)):
        if z_box[current_index] is not 0:
            if z_box[current_index] + current_index - 1 >= right_endpoints[current_index]:
                leftmost_endpoint = current_index

        left_endpoints[current_index] = leftmost_endpoint

    return left_endpoints


def test():
    z_input = "AABAABCAXAABAABCYAAAAB"
    z_box = find_z_box(z_input)
    right_endpoints = find_right_endpoints(z_input, z_box)
    left_endpoints = find_left_endpoints(z_input, z_box, right_endpoints)
    z_box[0] = 0

    # Formatting for printing
    test_string = [str(x) + " " for x in z_input]
    z_box = [str(x) + " " if x < 10 else str(x) for x in z_box]
    right_endpoints = [str(x) + " " if x < 10 else str(x) for x in right_endpoints]
    left_endpoints = [str(x) + " " if x < 10 else str(x) for x in left_endpoints]

    print(f"\n\n\tResults\n........................\n")
    print(f"Test string:                {test_string}")
    print(f"Resulting z-box:            {z_box}")
    print(f"Resulting right_endpoints:  {right_endpoints}")
    print(f"Resulting left_endpoints:   {left_endpoints}")

def run(pattern, input_string):
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
    
    print(f"\n\n\tResults\n........................\n")
    print(f"Test string:                {test_string}")
    print(f"Resulting z-box:            {z_box}")
    print(f"Resulting right_endpoints:  {right_endpoints}")
    print(f"Resulting left_endpoints:   {left_endpoints}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("pattern", help="pattern to search for")
    parser.add_argument("input_string", help="pattern to search for")
    args = parser.parse_args()
    run(args.pattern, args.input_string)
    # test()



