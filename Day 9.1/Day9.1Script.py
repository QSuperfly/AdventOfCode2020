from itertools import permutations

# Declare and assign some static information
example_filename = "Example.txt"
input_filename = "Input.txt"
output_filename = "Output.txt"

# Variables to use
preamble = 25

# Get list of lines from file input
def get_file_input():
    with open(input_filename, 'r') as file:
        file_list = file.read().splitlines()
    return file_list

# Loop through list and add values. Return False if no combo is found.
def XMAS_Looper(list_of_numbers, preamble):
    current_position = 0
    for number in list_of_numbers[:(preamble - 1)]:
        for number2 in list_of_numbers[current_position + 1:(preamble)]:
            print("Trying: " + str(number) + " + " + str(number2) + " = " + str(list_of_numbers[preamble]))
            if (int(number) + int(number2)) == int(list_of_numbers[preamble]):
                print("Found pair: " + str(number) + " + " + str(list_of_numbers[current_position + 1]) + " = " + list_of_numbers[preamble])
                return True
        current_position += 1
    print("No pair was found for: " + str(list_of_numbers[preamble]))
    return False

# XMAS Decrypter. Loop while pair is find.
def XMAS_Decrypter (list_of_numbers, preamble):
    while(XMAS_Looper(list_of_numbers, preamble)):
        list_of_numbers.pop(0)
        print("Combo found. Move one step.")
    return ""

# Lets get started!
print(XMAS_Decrypter(get_file_input(), preamble))