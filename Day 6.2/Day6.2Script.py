
# Declare and assign some static information
example_filename = "Example.txt"
input_filename = "Input.txt"
output_filename = "Output.txt"

# Variables to use
sum_of_yes_answers = 0
people_in_group = 0
valid_answers = 0
yes_questions = []

# Function that checks if everyone in the group answered Yes on the same question
def check_answers(yes_questions_unique, yes_questions, people_in_group):
    valid_answers = 0
    for s in yes_questions_unique:
        if yes_questions.count(s) == people_in_group:
            valid_answers += 1
    return valid_answers

# Read file and Loop through lines # More readable
line_counter = 0
for line in open(input_filename, 'r').readlines():
    line_counter += 1
    # print(line)
    if len(line.strip()) != 0:
        people_in_group += 1
        for s in line.rstrip():
            yes_questions.append(s)
        if (line_counter == len(open(input_filename).readlines(  ))):
            # print("EOF!")
            valid_answers += check_answers(list(set(yes_questions)), yes_questions, people_in_group)
    else:
        valid_answers += check_answers(list(set(yes_questions)), yes_questions, people_in_group)
        people_in_group = 0
        yes_questions = []

# Print answer
print("")
print("Sum of Yes answers: " + str(valid_answers))
