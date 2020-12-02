
# Variable to hold the count of valid passwords according to policy
valid_count = 0

# Read file and Loop through lines # Less code
# for line in open('input.txt', 'r').readlines(): 
#     line_parts = line.split(' ')
#     first_position = line_parts[0].split('-')[0]
#     second_position = line_parts[0].split('-')[1]
#     specific_letter = line_parts[1].split(':')[0]
#     if line_parts[2][int(first_position) - 1] == specific_letter and line_parts[2][int(second_position) - 1] != specific_letter:
#         valid_count += 1
#     if line_parts[2][int(first_position) - 1] != specific_letter and line_parts[2][int(second_position) - 1] == specific_letter:
#         valid_count += 1

# Read file and Loop through lines # Less code
for line in open('input.txt', 'r').readlines(): 
    if line.split(' ')[2][int(line.split(' ')[0].split('-')[0]) - 1] == line.split(' ')[1].split(':')[0] and line.split(' ')[2][int(line.split(' ')[0].split('-')[1]) - 1] != line.split(' ')[1].split(':')[0]:
        valid_count += 1
    if line.split(' ')[2][int(line.split(' ')[0].split('-')[0]) - 1] != line.split(' ')[1].split(':')[0] and line.split(' ')[2][int(line.split(' ')[0].split('-')[1]) - 1] == line.split(' ')[1].split(':')[0]:
        valid_count += 1

# Print answer
print (valid_count)