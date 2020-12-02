Lines = open('Input.txt', 'r').readlines()
for num1 in Lines:
    for num2 in Lines:
        for num3 in Lines:
            if((int(num1) + int(num2) + int(num3)) == 2020):
                print("num1 is: " + num1 + ", num2 is: " + num2 + ", num3 is: " + num3 + ", sum is: " + "{}".format(int(num1) + int(num2) + int(num3)))
                break