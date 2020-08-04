from print_helpers import *

def find_z_box(input_string, descriptive=False):
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

def z_algo_demo(input_string, descriptive=True):
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
            print(f"Matching P[{k}] to prefix")
            pattern_index = 0
            while pattern_index + k < len(input_string)\
             and input_string[pattern_index] == input_string[k + pattern_index]: 


                print(f"\nCurrent Index: {k}")
                print(f"Found new match: input[{k + pattern_index}] = {input_string[k + pattern_index]} = input[{pattern_index}] = {input_string[pattern_index]}")
                pretty_print_zbox(input_string, pattern_index, k)

                pattern_index += 1
            
            if pattern_index == 0 and descriptive:
                print(f"No match found; Inheriting r & l values")
            else :
                z_box[k] = pattern_index
                l = k
                r = l + pattern_index - 1
                if descriptive:
                    print(f"Match found! Updating r = {r} & l = {l}")

        else:
            print(f"\n################################################")
            pretty_print_current_index(input_string, k)
            print(f"\nIndex [{k}] - {input_string[k]} Case 2: z-box contains k")
            k_prime = k - l 
            beta = r - k + 1
            
            if z_box[k_prime] < beta:
                z_box[k] = z_box[k_prime]
                print(f"Case 2a: Z(k') = {z_box[k_prime]} < |B| = {beta} ")
                print(f"Inheriting z_box[k] = z_box[k_prime] = {z_box[k_prime]}")

            else:
                
                i = r + 1
                j = beta
                print(f"Case 2b: Z(k') = {z_box[k_prime]} ≥ |B| = {beta} ")
                print(f"Matching P[r + 1...] to P[B + 1...]")
                while i < len(input_string) and j < len(input_string) and input_string[i] == input_string[j]:
                    
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


def z_algo_streamlined(input_string, descriptive=True):
    z_box = [0] * len(input_string)
    r = 0
    l = 0
    
    if input_string[1] == input_string[0]:
        z_box[1] = z_box[1] + 1
        r = 1 
        l = 1

    # Algorithm portion: assume we know r & l at step k - 1
    for k in range(2, len(input_string)):
        
        if k > r: 
            pattern_index = 0
            while pattern_index + k < len(input_string)\
             and input_string[pattern_index] == input_string[k + pattern_index]: 

                pattern_index += 1
            
            if pattern_index != 0 :
                z_box[k] = pattern_index
                l = k
                r = l + pattern_index - 1
        else:
            k_prime = k - l 
            beta = r - k + 1
            
            if z_box[k_prime] < beta:
                z_box[k] = z_box[k_prime]
            
            else:
                i = r + 1
                j = beta
                while i < len(input_string) and j < len(input_string) and input_string[i] == input_string[j]:
                    i += 1
                    j +=1
                    
                z_box[k] = i - k
                l = k
                r = i - 1
    return z_box








