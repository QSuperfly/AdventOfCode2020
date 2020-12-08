
# Declare and assign some static information
example_filename = "Example.txt"
input_filename = "Input.txt"
output_filename = "Output.txt"

# Variables to use
bag_to_check = "shiny gold"

# Get list of lines from file input
def get_file_input():
    with open(input_filename, 'r') as file:
        file_list = file.read().splitlines()
    return file_list

# Recursive function that checks which bags can hold the specified bag
def check_main_bag_occurances (bag_to_check, list_of_bags, number_of_bags):
    total_bags = 1
    for bag in list_of_bags:
        if bag_to_check in bag.split(" bags contain ")[0]:
            for contains_bag in bag.split(" bags contain ")[1].rstrip().replace(".", "").replace("bags", "").replace("bag", "").split(", "):
                if "no other" not in contains_bag:
                    total_bags += int(contains_bag.split(" ")[0]) * check_main_bag_occurances(contains_bag.replace(contains_bag.split(" ")[0] + " ", "").rstrip(), list_of_bags, int(contains_bag.split(" ")[0]))
    return total_bags

# Print answer
print("")
print("Done! Result: " + str(check_main_bag_occurances(bag_to_check, get_file_input(), 1) - 1))