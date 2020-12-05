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
                                print("Valid!")
                                return 1
    print ("Not Valid!")
    return 0

# Read file and Loop through lines # More readable
line_counter = 0
for line in open(input_filename, 'r').readlines():
    line_counter += 1
    if len(line.strip()) != 0: 
        line_parts = line.split(' ')
        for passport_attribute in line_parts:
            current_passport.append(passport_attribute.split(':')[0]) # Append the attributes to the "passport"
        # Check if end of file was reached
        if (line_counter == len(open(input_filename).readlines(  ))):
            print ("Reached EOF!")
            #print ("Checking passport: " + current_passport)
            print('Checking Passport: [%s]' % ', '.join(map(str, current_passport)))
            valid_passports += check_passport(current_passport)
            total_passports += 1
            current_passport = []
    else:
        #print ("Checking passport: " + current_passport)
        print('Checking Passport: [%s]' % ', '.join(map(str, current_passport)))
        valid_passports += check_passport(current_passport)
        total_passports += 1
        current_passport = []

# Print answer
print("Total passports: " + str(total_passports) + ", Valid passports: " + str(valid_passports))