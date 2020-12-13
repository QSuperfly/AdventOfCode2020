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

# Recursive function that loops through numbers list and adds them up till the number is equal or greater than the end goal number.
def check_contaginous_numbers(list_of_numbers, final_result, end_index):
    #print("check_contaginous_numbers final_result: " + final_result)
    current_total = 0
    smallest_number = 100000000
    largest_number = -1
    for number in list_of_numbers:
        current_total += int(number)
        #print("current_total: " + str(current_total))
        if int(number) != final_result:
            if int(number) < int(smallest_number):
                smallest_number = number
            if int(number) > int(largest_number):
                largest_number = number
            if int(current_total)  == int(final_result):
                print ("Found smallest and largets number: " + str(smallest_number) + " and " + str(largest_number) + ", End result: " + str(int(smallest_number) + int(largest_number)))
            if int(current_total) > int(final_result):
                check_contaginous_numbers(list_of_numbers[1:], final_result, end_index)
                break
    return ""

# Loop through list and add values. Return False if no combo is found.
def XMAS_Looper(list_of_numbers, preamble):
    current_position = 0
    for number in list_of_numbers[:(preamble - 1)]:
        for number2 in list_of_numbers[current_position + 1:(preamble)]:
            #print("Trying: " + str(number) + " + " + str(number2) + " = " + str(list_of_numbers[preamble]))
            if (int(number) + int(number2)) == int(list_of_numbers[preamble]):
                #print("Found pair: " + str(number) + " + " + str(list_of_numbers[current_position + 1]) + " = " + list_of_numbers[preamble])
                return True
        current_position += 1
    #print("No pair was found for: " + str(list_of_numbers[preamble]))
    check_contaginous_numbers(get_file_input()[0: get_file_input().index(str(list_of_numbers[preamble])) + 1], str(list_of_numbers[preamble]), get_file_input().index(str(list_of_numbers[preamble])))
    return False

# XMAS Decrypter. Loop while pair is find.
def XMAS_Decrypter (list_of_numbers, preamble):
    while(XMAS_Looper(list_of_numbers, preamble)):
        list_of_numbers.pop(0)
        #print("Combo found. Move one step.")
    return ""

# Lets get started!
print(XMAS_Decrypter(get_file_input(), preamble))