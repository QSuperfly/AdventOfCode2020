
# Variable to hold the count of valid passwords according to policy
valid_count = 0

# Read file and Loop through lines # More readable
# for line in open('input.txt', 'r').readlines(): 
#     line_parts = line.split(' ')
#     min_count = line_parts[0].split('-')[0]
#     max_count = line_parts[0].split('-')[1]
#     specific_letter = line_parts[1].split(':')[0]
#     specific_letter_count = line_parts[2].count(line_parts[1].split(':')[0])
#     if int(min_count) <= int(line_parts[2].count(line_parts[1].split(':')[0])) <= int(max_count):
#         valid_count += 1

# Read file and Loop through lines # Less code
for line in open('input.txt', 'r').readlines(): 
    if int(line.split(' ')[0].split('-')[0]) <= int(line.split(' ')[2].count(line.split(' ')[1].split(':')[0])) <= int(line.split(' ')[0].split('-')[1]):
        valid_count += 1

# Print answer
print (valid_count)