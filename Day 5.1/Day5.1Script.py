
# Declare and assign some static information
example_filename = "Example.txt"
input_filename = "Input.txt"
output_filename = "Output.txt"

# Variables to use
max_row = 128
min_row = 0
max_column = 8
min_column = 0
row = -1
seat = -1
seat_id_current_max = 0
highest_seat_id = 0

# Calculate the Seat ID
def calculate_seat_id (row, seat):
    #print ("Calculating: " + str(row) + "* 8 + " + str(seat))
    return (row * 8) + seat

# Check passport data
def check_passport_data (passport):
    return ""

# Read file and Loop through lines # More readable
line_counter = 0
for line in open(input_filename, 'r').readlines():
    print(line)
    max_row = 128
    min_row = 0
    max_column = 8
    min_column = 0
    found_row = False
    found_seat = False
    row = -1
    seat = -1
    for s in line:
        if found_row:
            if (s == 'L'):
                max_column = min_column + ((max_column - min_column) / 2)
                #print ("L Lower: " + str(max_column))
                if( (int(max_column) - 1) == int(min_column) ):
                    print("Found seat: " + str(int(max_column) - 1))
                    seat = max_column - 1
                    found_seat = True
                    break
            else:
                min_column += ((max_column - min_column) / 2)
                #print ("R Upper: " + str(min_column))
                if( (int(max_column) - 1) == int(min_column) ):
                    print("Found seat: " + str(int(max_column) - 1))
                    seat = max_column - 1
                    found_seat = True
                    break
        else:
            if (s == 'F'):
                max_row = min_row + ((max_row - min_row) / 2)
                #print ("F Lower: " + str(max_row))
                if ((int(max_row) - 1) == int(min_row) ):
                    print("Found row: " + str(int(max_row) - 1))
                    row = max_row - 1
                    found_row = True
            else:
                min_row += ((max_row - min_row) / 2)
                #print ("B Upper: " + str(min_row))
                if ((int(max_row) - 1) == int(min_row) ):
                    print("Found row: " + str(int(max_row) - 1))
                    row = max_row - 1
                    found_row = True    
    if (int(calculate_seat_id(row, seat)) > highest_seat_id):
        highest_seat_id = int(calculate_seat_id(row, seat))
    print("Seat ID: " + str(int(calculate_seat_id(row, seat))))
    print("")
# Print answer
print("")
print("Highest Seat ID: " + str(highest_seat_id))

# Wrong ansers