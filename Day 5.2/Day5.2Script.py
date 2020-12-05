
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
seat_ids = []

# Calculate the Seat ID
def calculate_seat_id (row, seat):
    #print ("Calculating: " + str(row) + "* 8 + " + str(seat))
    return (row * 8) + seat

# Find my seat!
def find_my_seat (seat_ids):
    total_seat_ids_next_to_mine = 0
    for i, seat_id in enumerate(seat_ids):
        if(i > 0):
            try:
                if ((seat_id - seat_ids[i-1]) - (seat_ids[i+1] - seat_id) != 0):
                    total_seat_ids_next_to_mine += seat_id
            except IndexError:
                print("IndexError")
    return str(total_seat_ids_next_to_mine / 2)

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
    seat_ids.append(int(calculate_seat_id(row, seat)))
    print("Seat ID: " + str(int(calculate_seat_id(row, seat))))
    print("")

#seat_ids = sorted(seat_ids)
print(sorted(seat_ids))

# Print answer
print("")
print("My seat is: " + find_my_seat(sorted(seat_ids)))

# Wrong ansers