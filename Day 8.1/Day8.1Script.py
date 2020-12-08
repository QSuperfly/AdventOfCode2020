import re

# Declare and assign some static information
example_filename = "Example.txt"
input_filename = "Input.txt"
output_filename = "Output.txt"

# Variables to use
accumulator = 0
jumps = 0
no_operation = 0

# Get list of lines from file input
def get_file_input():
    with open(input_filename, 'r') as file:
        file_list = file.read().splitlines()
    return file_list

# Recursive function that checks which bags can hold the specified bag
def instruction_executor (instruction_position, instructions):
    accumulator =0
    print("Instruction at position: " + str(instruction_position) + ", instruction: " + instructions[instruction_position])
    if "Executed" not in instructions[instruction_position]:
        if "nop" in instructions[instruction_position]:
            instructions[instruction_position] = "Executed"
            print("Jumping to: " + str(instruction_position + 1))
            accumulator += instruction_executor(instruction_position + 1, instructions)
        elif "acc" in instructions[instruction_position]:
            accumulator += int(instructions[instruction_position].split(" ")[1])
            print("Jumping to: " + str(instruction_position + 1) + ", after adding to accumulator: " + str(int(instructions[instruction_position].split(" ")[1])))
            instructions[instruction_position] = "Executed"
            accumulator += instruction_executor(instruction_position + 1, instructions)
        elif "jmp" in instructions[instruction_position]:
            new_instruction_position = instruction_position + int(instructions[instruction_position].split(" ")[1])
            instructions[instruction_position] = "Executed"
            print ("Jumping to: " + str(new_instruction_position))
            accumulator += instruction_executor(new_instruction_position, instructions)
    return accumulator

# Print answer
print("")
print("Done! Result: " + str(instruction_executor(0, get_file_input())))