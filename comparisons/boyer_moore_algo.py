"""
Original source code: https://github.com/TheAlgorithms/Python/blob/master/strings/boyer_moore_search.py

The algorithm finds the pattern in given input_string using following rule.

The bad-character rule considers the mismatched character in input_string.
The next occurrence of that character to the left in Pattern is found,

If the mismatched character occurs to the left in Pattern,
a shift is proposed that aligns input_string block and pattern.

If the mismatched character does not occur to the left in Pattern,
a shift is proposed that moves the entirety of Pattern past
the point of mismatch in the input_string.

If there no mismatch then the pattern matches with input_string block.

Time Complexity : O(n/m)
    n=length of main string
    m=length of pattern string
"""
import argparse

def match_in_pattern(pattern, char):
    """ finds the index of char in pattern in reverse order

    Parameters :
        char (chr): character to be searched

    Returns :
        i (int): index of char from last in pattern
        -1 (int): if char is not found in pattern
    """

    for i in range(len(pattern) - 1, -1, -1):
        if char == pattern[i]:
            return i
    return -1

def mismatch_in_input_string(pattern, input_string, currentPos):
    """
    find the index of mis-matched character in input_string when compared with pattern
    from last

    Parameters :
        currentPos (int): current index position of input_string

    Returns :
        i (int): index of mismatched char from last in input_string
        -1 (int): if there is no mismatch between pattern and input_string block
    """

    for i in range(len(pattern) - 1, -1, -1):
        if pattern[i] != input_string[currentPos + i]:
            return currentPos + i
    return -1

def bad_character_heuristic(pattern, input_string):
    # searches pattern in input_string and returns index positions
    positions = []
    for i in range(len(input_string) - len(pattern) + 1):
        mismatch_index = mismatch_in_input_string(pattern, input_string, i)
        if mismatch_index == -1:
            positions.append(i)
        else:
            match_index = match_in_pattern(pattern, input_string[mismatch_index])
            i = (mismatch_index - match_index)  
    return positions

def bm(pattern, input_string):
    positions = bad_character_heuristic(pattern, input_string)

    if len(positions) == 0:
        print("No match found")
    else:
        print("Pattern found in following positions: ")
        print(positions)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("pattern", help="pattern to search for")
    parser.add_argument("input_string", help="pattern to search for")
    args = parser.parse_args()
    bm(args.pattern, args.input_string)

