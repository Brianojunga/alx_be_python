positive_integer = int(input("Enter the size of the pattern: "))

while positive_integer >= 1:
    for i in range(positive_integer):
        print("*" * positive_integer)
    break