
# Declare and assign some static information
example_filename = "Example.txt"
input_filename = "Input.txt"
output_filename = "Output.txt"

# Variables to use
bag_to_check = "shiny gold bag"

# Get list of lines from file input
def get_file_input():
    with open(input_filename, 'r') as file:
        file_list = file.read().splitlines()
    return file_list

# Create dictionary item
def create_dictionary_item(bag):
    print(bag[:bag.find(" bags contain ")])
    this_bag = {
        "bag": bag[:bag.find(" bags contain ")]
    }
    for s in bag[bag.find(" bags contain "):].replace(" bags contain ", "").replace(".", "").split(", "):
        print("Count " + str(s.split(" ")[0]))
    return this_bag

# Recursive function that checks which bags can hold the specified bag
def check_main_bag_occurances (bag_to_check, list_of_bags):
    list_of_possible_bags = []
    for bag in list_of_bags:
        #print(bag[bag.find(" bags contain "):].replace(" bags contain ", "").replace(".", "").split(", "))
        if bag_to_check in bag[bag.find(" bags contain "):]:
            print (bag_to_check)
            #list_of_possible_bags.append(bag[:bag.find(" bags contain ")])
            list_of_possible_bags.append(create_dictionary_item(bag))
            #print(bag[:bag.find(" bags contain ")]+ " " + str(bag.find(bag_to_check)))
            #print (bag[bag.find(" bags contain "):].replace(" bags contain ", "").replace(".", "").split(", "))
            #print(list_of_possible_bags)
            list_of_possible_bags.extend(check_main_bag_occurances(bag[:bag.find(" bags contain ")], list_of_bags))
    return list_of_possible_bags

# Print answer
print("")
#print("Sum of bags: " + str(len(set(check_main_bag_occurances(bag_to_check, get_file_input())))))
print(list(check_main_bag_occurances(bag_to_check, get_file_input())))

# Wrong answers
# 100