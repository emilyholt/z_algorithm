import time

from colorama import init, Fore, Back, Style

init()

def pretty_print_current_index(input_string, current_index):
    time.sleep(0.5)
    beginning_string = "["
    current_string = ""
    end_string = ""

    beginning_indices_string = "["
    current_index_string = ""
    ending_indices_string = ""

    # Separate the pattern & z-boxes into strings
    for i, elem in enumerate(input_string):
        if i < current_index:
            beginning_string = beginning_string + str(elem) + " , "
            if i < 10:
                beginning_indices_string = beginning_indices_string + str(i) + " , "  
            else:
                beginning_indices_string = beginning_indices_string + str(i) + ", "

        elif i == current_index:
            current_string = current_string + str(elem) + " "
            if current_index < 10:
                current_index_string = current_index_string + str(current_index) + " "  
            else: 
                current_index_string = current_index_string + str(current_index)

        elif i > current_index and i < len(input_string) - 1:
            end_string = end_string + str(elem) + " , "
            if i < 10: 
                ending_indices_string = ending_indices_string + str(i) + " , " 
            else: 
                ending_indices_string = ending_indices_string + str(i) + ", "
        
        else:
            end_string = end_string + str(elem)
            ending_indices_string = ending_indices_string + str(i) 

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
    time.sleep(0.5)
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