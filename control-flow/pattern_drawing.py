# Enter a positive interger and the script will draw a pattern that matches it.

input = int(input("Enter the size of the pattern:"))

while input >0:
    for i in range(input):
        print("*" * (i+1))
        input -=1
    print("*", end="")
