import argparse
from colorama import init, Fore, Back, Style

init()

def pretty_print_current_index(input_string, current_index):
    beginning_string = "["
    current_string = ""
    end_string = ""

    beginning_indices_string = "["
    current_index_string = ""
    ending_indices_string = ""

    # Separate the pattern & z-boxes into strings
    for i, elem in enumerate(input_string):
        if i < current_index:
            beginning_string = beginning_string + str(elem) + ", "
            beginning_indices_string = beginning_indices_string + str(i) + " , " if i < 10 else beginning_indices_string + str(i) + ", "

        elif i == current_index:
            current_string = current_string + str(elem) 
            current_index_string = current_index_string + str(current_index) + " " if current_index < 10 else current_index_string + str(current_index)

        elif i > current_index and i < len(input_string) - 1:
            end_string = end_string + str(elem) + ", "
            ending_indices_string = ending_indices_string + str(i) + " , " if i < 10 else ending_indices_string + str(i) + ", "
        
        else:
            end_string = end_string + str(elem)
            ending_indices_string = ending_indices_string + str(i) if i < 10 else ending_indices_string + str(i)

    # Pretty printing of our color-coded z-box
    if current_index < len(input_string) - 1:
        print(Fore.RESET + beginning_string
        + Fore.RED + current_string
        + Fore.RESET + ", " + end_string  + "]"
        , end='\n')

        print(Fore.RESET + beginning_indices_string
            + Fore.RED + current_index_string
            + Fore.RESET + ", " + ending_indices_string + "]"
            , end='\n')
    else:
        print(Fore.RESET + beginning_string
            + Fore.RED + current_string
            + Fore.RESET + "]"
            , end='\n')

        print(Fore.RESET + beginning_indices_string
            + Fore.RED + current_index_string
            + Fore.RESET+ "]"
            , end='\n')

    


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

def z_algo(input_string, descriptive=True):
    z_box = [0] * len(input_string)
    r = 0
    l = 0

    print(f"\n################################################")
    print(f"Brute Force Portion: Case i = 2")
    if input_string[1] != input_string[0]:
        print(f"* Case 1: No match; Z2 = r = l = 0")
    else:
        print(f"* Case 2: Match! Z2 = r = l = 1")
        z_box[1] = z_box[1] + 1
        r = 1 
        l = 1

    # Algorithm portion: assume we know r & l at step k - 1
    for k in range(2, len(input_string)):
        
        if k > r:
            print(f"\n################################################")
            pretty_print_current_index(input_string, k)
            print(f"\nIndex [{k}] Case 1: No z-box jumps over k")
            print(f"Matching P[{k}] tp prefix")
            pattern_index = 0
            while pattern_index + k < len(input_string)\
             and input_string[pattern_index] == input_string[k + pattern_index]: 

                if descriptive:
                    print(f"\nCurrent Index: {k}")
                    print(f"Found new match: input[{k + pattern_index}] = {input_string[k + pattern_index]} = input[{pattern_index}] = {input_string[pattern_index]}")
                    pretty_print_zbox(input_string, pattern_index, k)

                pattern_index += 1
            
            if pattern_index == 0:
                print(f"No match found; Inheriting r & l values")
            else :
                z_box[k] = pattern_index
                l = k
                r = l + pattern_index - 1
                print(f"Match found! Updating r = {r} & l = {l}")

        else:
            print(f"\n################################################")
            pretty_print_current_index(input_string, k)
            print(f"\nIndex [{k}] - {input_string[k]} Case 2: z-box contains k")
            k_prime = k - l 
            beta = r - k + 1
            
            if z_box[k_prime] < beta:
                print(f"Case 2a: Z(k') = {z_box[k_prime]} < |B| = {beta} ")
                z_box[k] = z_box[k_prime]
                print(f"Inheriting z_box[k] = z_box[k_prime] = {z_box[k_prime]}")

            else:
                print(f"Case 2b: Z(k') = {z_box[k_prime]} ≥ |B| = {beta} ")
                i = r + 1
                j = beta
                print(f"Matching P[r + 1...] to P[B + 1...]")
                while i < len(input_string) and j < len(input_string) and input_string[i] == input_string[j]:
                    
                    if descriptive:
                        print(f"\nCurrent Index: {k}")
                        print(f"Found new match: input[{i}] = {input_string[i]} = input[{j}] = {input_string[j]}")
                        pretty_print_zbox(input_string, j, k)
                    i += 1
                    j +=1
                    
                z_box[k] = i - k
                l = k
                r = i - 1
                print(f"Updating r = {r} & l = {l}")
    return z_box

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
    
    print(f"\n\n\tResults\n........................\n")
    print(f"Test string:                {test_string}")
    print(f"Resulting z-box:            {z_box}")
    print(f"Resulting right_endpoints:  {right_endpoints}")
    print(f"Resulting left_endpoints:   {left_endpoints}")

def run(pattern, input_string):
    z_input = pattern + "$" + input_string
    z_input = "AABAABCAXAABAABCYAAAAB"
    z_box = z_algo(z_input)

    # Formatting for printing
    indices = [str(x) + " " if x < 10 else str(x) for x in range(len(z_input))]
    test_string = [str(x) + " " for x in z_input]
    z_box = [str(x) + " " if x < 10 else str(x) for x in z_box]
    
    print(f"\n################################################")
    print(f"\n\tResults\n........................\n")
    print(f"Indices:                    {indices}")
    print(f"Test string:                {test_string}")
    print(f"Resulting z-box:            {z_box}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("pattern", help="pattern to search for")
    parser.add_argument("input_string", help="pattern to search for")
    args = parser.parse_args()
    run(args.pattern, args.input_string)



