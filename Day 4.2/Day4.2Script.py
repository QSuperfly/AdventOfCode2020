import re

# Declare and assign some static information
input_filename = "Input.txt"
output_filename = "Output.txt"

# Variables to hold the count of trees along the path, and where we are right now in the slope/forest.
total_passports = 0
valid_passports = 0
is_valid = False
current_passport = []

# Check if passport is valid function
def check_passport (passport):
    # if any(('byr' and 'iyr' and 'eyr' and 'hgt' and 'hcl' and 'ecl' and 'pid') in s for s in passport):
    if 'byr' in passport:
        if 'iyr' in passport:
            if 'eyr' in passport:
                if 'hgt' in passport:
                    if 'hcl' in passport:
                        if 'ecl' in passport:
                            if 'pid' in passport:
                                #print("Valid!")
                                return 1
    #print ("Not Valid!")
    return 0

# Check passport data
def check_passport_data (passport):
    return ""

# Read file and Loop through lines # More readable
line_counter = 0
for line in open('input.txt', 'r').readlines():
    line_counter += 1
    if len(line.strip()) != 0: 
        line_parts = line.split(' ')
        for passport_attribute in line_parts:
            #print("Checking: " + passport_attribute.split(':')[0] + ", value: " + passport_attribute.split(':')[1])
            if (passport_attribute.split(':')[0] == 'byr'):
                if (int(passport_attribute.split(':')[1]) >= 1920 and int(passport_attribute.split(':')[1]) <= 2002):
                    current_passport.append(passport_attribute.split(':')[0]) # Append the attributes to the "passport"
                    print("Ok [byr]! " + passport_attribute.split(':')[1])
                else:
                    print("Not ok [byr]! " + passport_attribute.split(':')[1])
            elif (passport_attribute.split(':')[0] == 'iyr'):
                if (int(passport_attribute.split(':')[1]) >= 2010 and int(passport_attribute.split(':')[1]) <= 2020):
                    current_passport.append(passport_attribute.split(':')[0]) # Append the attributes to the "passport"
                    print("Ok [iyr]! " + passport_attribute.split(':')[1])
                else:
                    print("Not ok [iyr]! " + passport_attribute.split(':')[1])
            elif (passport_attribute.split(':')[0] == 'eyr'):
                if (int(passport_attribute.split(':')[1]) >= 2020 and int(passport_attribute.split(':')[1]) <= 2030):
                    current_passport.append(passport_attribute.split(':')[0]) # Append the attributes to the "passport"
                    print("Ok [eyr]! " + passport_attribute.split(':')[1])
                else:
                    print("Not ok [eyr]! " + passport_attribute.split(':')[1])
            elif (passport_attribute.split(':')[0] == 'hgt'):
                if ("cm" in passport_attribute.split(':')[1]):
                    if (int(passport_attribute.split(':')[1].strip()[:-2]) >= 150 and int(passport_attribute.split(':')[1].strip()[:-2]) <= 193):
                        current_passport.append(passport_attribute.split(':')[0]) # Append the attributes to the "passport"
                        print("Ok [hgt]! " + passport_attribute.split(':')[1])
                    else:
                        print("Not ok [hgt]! " + passport_attribute.split(':')[1])
                elif ("in" in passport_attribute.split(':')[1]):
                    if (int(passport_attribute.split(':')[1].strip()[:-2]) >= 59 and int(passport_attribute.split(':')[1].strip()[:-2]) <= 76):
                        current_passport.append(passport_attribute.split(':')[0]) # Append the attributes to the "passport"
                        print("Ok [hgt]! " + passport_attribute.split(':')[1])
                    else:
                        print("Not ok [hgt]! " + passport_attribute.split(':')[1])
            elif (passport_attribute.split(':')[0] == 'hcl'):
                if (re.search("^#[a-f0-9]{6,6}", passport_attribute.split(':')[1])):
                    current_passport.append(passport_attribute.split(':')[0]) # Append the attributes to the "passport"
                    print("Ok [hcl]! " + passport_attribute.split(':')[1])
                else:
                    print("Not ok [hcl]! " + passport_attribute.split(':')[1])
            elif (passport_attribute.split(':')[0] == 'ecl'):
                if 'amb' in passport_attribute.split(':')[1]:
                    current_passport.append(passport_attribute.split(':')[0]) # Append the attributes to the "passport"
                    print("Ok [ecl]! " + passport_attribute.split(':')[1])
                elif 'blu' in passport_attribute.split(':')[1]:
                    current_passport.append(passport_attribute.split(':')[0]) # Append the attributes to the "passport"
                    print("Ok [ecl]! " + passport_attribute.split(':')[1])
                elif 'brn' in passport_attribute.split(':')[1]:
                    current_passport.append(passport_attribute.split(':')[0]) # Append the attributes to the "passport"
                    print("Ok [ecl]! " + passport_attribute.split(':')[1])
                elif 'gry' in passport_attribute.split(':')[1]:
                    current_passport.append(passport_attribute.split(':')[0]) # Append the attributes to the "passport"
                    print("Ok [ecl]! " + passport_attribute.split(':')[1])
                elif 'grn' in passport_attribute.split(':')[1]:
                    current_passport.append(passport_attribute.split(':')[0]) # Append the attributes to the "passport"
                    print("Ok [ecl]! " + passport_attribute.split(':')[1])
                elif 'hzl' in passport_attribute.split(':')[1]:
                    current_passport.append(passport_attribute.split(':')[0]) # Append the attributes to the "passport"
                    print("Ok [ecl]! " + passport_attribute.split(':')[1])
                elif 'oth' in passport_attribute.split(':')[1]:
                    current_passport.append(passport_attribute.split(':')[0]) # Append the attributes to the "passport"
                    print("Ok [ecl]! " + passport_attribute.split(':')[1])
                else:
                    print("Not ok [ecl]! " + passport_attribute.split(':')[1])
            elif (passport_attribute.split(':')[0] == 'pid'):
                if (re.search("^[0-9]{9,9}", passport_attribute.split(':')[1])):
                    current_passport.append(passport_attribute.split(':')[0]) # Append the attributes to the "passport"
                    print("Ok [pid]! " + passport_attribute.split(':')[1])
                else:
                    print("Not ok [pid]! " + passport_attribute.split(':')[1])
        # Check if end of file was reached
        if (line_counter == len(open(input_filename).readlines(  ))):
            #print ("Reached EOF!")
            #print ("Checking passport: " + current_passport)
            #print('Checking Passport: [%s]' % ', '.join(map(str, current_passport)))
            valid_passports += check_passport(current_passport)
            total_passports += 1
            current_passport = []
    else:
        #print ("Checking passport: " + current_passport)
        #print('Checking Passport: [%s]' % ', '.join(map(str, current_passport)))
        valid_passports += check_passport(current_passport)
        total_passports += 1
        current_passport = []

# Print answer
print("Total passports: " + str(total_passports) + ", Valid passports: " + str(valid_passports))

# Wrong ansers
# 132