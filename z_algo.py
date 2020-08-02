
def find_z_box(input_string):
    z_box = [0] * len(input_string)
    
    left_endpoints = [0] * len(input_string)
    
    for current_index in range(1, len(input_string)):
        pattern_index = 0
        while pattern_index + current_index < len(input_string)\
         and input_string[pattern_index] == input_string[pattern_index + current_index]:
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
            # print(f"At Index [{current_index}]; z-box = {z_box[current_index]}; right_endpoints = {right_endpoints[current_index]}")
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

    test_string = [str(x) + " " for x in z_input]
    z_box = [str(x) + " " if x < 10 else str(x) for x in z_box]
    right_endpoints = [str(x) + " " if x < 10 else str(x) for x in right_endpoints]
    left_endpoints = [str(x) + " " if x < 10 else str(x) for x in left_endpoints]

    print(f"Test string:                {test_string}")
    print(f"Resulting z-box:            {z_box}")
    print(f"Resulting right_endpoints:  {right_endpoints}")
    print(f"Resulting left_endpoints:   {left_endpoints}")

if __name__ == '__main__':
    test()