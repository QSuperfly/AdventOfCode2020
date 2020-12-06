
# Declare and assign some static information
example_filename = "Example.txt"
input_filename = "Input.txt"
output_filename = "Output.txt"

# Variables to use
sum_of_yes_answers = 0
yes_questions = []

# Read file and Loop through lines # More readable
for line in open(input_filename, 'r').readlines():
    # print(line)
    if len(line.strip()) != 0:
        for s in line.rstrip():
            if s not in yes_questions:
                yes_questions.append(s)
                sum_of_yes_answers += 1
    else:
        yes_questions = []

# Print answer
print("")
print("Sum of Yes answers: " + str(sum_of_yes_answers))
