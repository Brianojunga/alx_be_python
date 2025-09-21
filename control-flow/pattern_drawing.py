size = int(input("Enter the size of the pattern: "))

row = 0
while row < size:              # while loop controls rows
    for col in range(size):    # for loop controls columns
        print("*", end="")     # print stars side by side
    print()                    # move to next line after finishing a row
    row += 1