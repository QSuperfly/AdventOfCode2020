Lines = open('Input.txt', 'r').readlines()
count = 0
for num1 in Lines:
    for num2 in Lines:
        if((int(num1) + int(num2)) == 2020):
            print("num1 is: " + num1 + ", num2 is: " + num2 + ", sum is: " + "{}".format(int(num1) + int(num2)))