# Declare and assign some static information
input_filename = "Input.txt"
output_filename = "Output.txt"

# Variables to hold the count of trees along the path, and where we are right now in the slope/forest.
trees_count = 0
current_row = 0
current_column = 0

# Function that returns row count in input file
def get_file_row_count(fileName):
    with open(fileName) as f:
        for i, l in enumerate(f):
            pass
        return i + 1

# Function for writing the forest to output file, just for clarity
def write_forest_to_file(fileName, forest):
    with open(fileName, "w") as txt_file:
        for line in forest:
            txt_file.write("".join(line) + "\n")

# Function to "move" us along the path
def travel_down_the_slope(forest, trees_count):
    return check_if_tree(int(current_row), int(current_column), forest, trees_count)

# Function that checks if we met a tree at the given position
def check_if_tree(x, y, forest, trees_count):
    print("" + str(x) + " " + str(y))
    if forest[int(x)][int(y)] == "#":
        forest[int(x)][int(y)] = "X"
        return 1
    else:
        forest[int(x)][int(y)] = "O"
    return 0

# Create multi dimensional array with all data
forest = []
for line in open(input_filename, "r").read().splitlines():
    row = []
    for x in range(35):
        for placement in line:
            row.append(placement)
    forest.append(row)

print("Number of rows: " + str(len(forest)) + ", Number of cols: " + str(len(forest[0])))

# Start traveling down the slope!
for lines in forest:
    if current_row < (len(forest) - 1):
        current_row += 1
        current_column += 3
        trees_count += travel_down_the_slope(forest, trees_count)

# Write the forest to file
write_forest_to_file(output_filename, forest)

# Print answer
print(trees_count) # 178