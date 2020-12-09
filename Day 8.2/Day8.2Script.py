import re

# Declare and assign some static information
example_filename = "Example.txt"
input_filename = "Input.txt"
output_filename = "Output.txt"

# Variables to use

# Get list of lines from file input
def get_file_input():
    with open(input_filename, 'r') as file:
        file_list = file.read().splitlines()
    return file_list

# Check result
def check_result(result):
    if result > -1000000000000:
        print ("Done! Result is: " + str(result))
        print ("")
        return True
    else:
        return False

# Try every case, replace nop with jmp or jmp with nop
def instruction_replacer(instruction_position, instructions):
    for instruction in instructions:
        new_instructions = get_file_input()
        if "nop" in instruction:
            if int(instruction.split(" ")[1]) != 0:
                new_instructions[instruction_position] = new_instructions[instruction_position].replace("nop", "jmp")
                result = instruction_executor(0, new_instructions)
                if check_result(result):
                    break
        if "jmp" in instruction:
            new_instructions[instruction_position] = new_instructions[instruction_position].replace("jmp", "nop")
            result = instruction_executor(0, new_instructions)
            if check_result(result):
                break
        instruction_position += 1
    return ""

# Recursive function that checks the instructions, executes it and calls itself for the next instruction
def instruction_executor (instruction_position, instructions):
    accumulator = 0
    if instruction_position < len(instructions): # Check if end of file was not reached
        if "Executed" not in instructions[instruction_position]:
            if "nop" in instructions[instruction_position]:
                instructions[instruction_position] = "Executed"
                accumulator += instruction_executor(instruction_position + 1, instructions)
            elif "acc" in instructions[instruction_position]:
                accumulator += int(instructions[instruction_position].split(" ")[1])
                instructions[instruction_position] = "Executed"
                accumulator += instruction_executor(instruction_position + 1, instructions)
            elif "jmp" in instructions[instruction_position]:
                new_instruction_position = instruction_position + int(instructions[instruction_position].split(" ")[1])
                instructions[instruction_position] = "Executed"
                accumulator += instruction_executor(new_instruction_position, instructions)
        else:
            #print ("Previously executed instruction was reached.. This is not the right answer. :(")
            return -10000000000000
    else:
        print ("")
        print ("End of file was reached!")
    return accumulator

# Lets get started!
instruction_replacer(0, get_file_input())