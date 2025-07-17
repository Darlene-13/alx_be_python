# This script promptsba user to input  a number then generates the multiplication table for the same from the numbers 1 and 10
number = input("Enter a number to see its multiplication table:")
print(f"Multiplication table for {number} is:")

for i in range (1,11):
    result = int(number) * i
    print(f"{number} * {i} = {result}")

