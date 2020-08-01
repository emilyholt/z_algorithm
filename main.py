import argparse

def find_z_box(input_string):
    z_box = [0] * len(input_string)
    right_endpoints = [0] * len(input_string)
    left_endpoints = [0] * len(input_string)
    
    for current_index in range(1, len(input_string)):

        # If we are outside the most recent z-box, we need to check if we have a match
        if current_index > right_endpoints[current_index - 1]:

            pattern_index = 0

            # Loop over string and calculate longest string starting at input_string(i) & matching prefix of input_string 
            while input_string[pattern_index] == input_string[current_index + pattern_index] \
             and current_index + pattern_index  < len(input_string) - 1:
                pattern_index += 1

            # If we matched at least one character, update boxes & endpoints
            if pattern_index > 0:
                # Store the number of characters matched
                z_box[current_index] = pattern_index + 1
                right_endpoints[current_index] = current_index + pattern_index
                left_endpoints[current_index] = current_index

        # Otherwise, we're still inside the current z-box
        else:
            pass
            '''
            pair_index = current_index - left_endpoints[current_index] 
            right_part_len = right_endpoints[current_index] - current_index + 1

            if z_box[pair_index] < right_part_len:
                z_box[current_index] = z_box[pair_index]
            
            else:
                i = right_endpoints[current_index] + 1
                while i < len(input_string) and input_string[i] == input_string[i - current_index]:
                    i += 1
                z_box[current_index] = i - current_index

                left_endpoints[current_index] = current_index
                right_endpoints[current_index] = i - 1
            '''

    return z_box, right_endpoints, left_endpoints
    

def main(pattern, input_string):
    z_input = pattern + "$" + input_string
    z_box, right_endpoints, left_endpoints = find_z_box(z_input)
    pattern_len = len(pattern) + 1 
    print(f"Resulting z-box:            {z_box[pattern_len:]}")
    print(f"Resulting right_endpoints:  {right_endpoints[pattern_len:]}")
    print(f"Resulting left_endpoints:   {left_endpoints[pattern_len:]}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("pattern", help="pattern to search for")
    parser.add_argument("input_string", help="pattern to search for")
    args = parser.parse_args()
    main(args.pattern, args.input_string)

