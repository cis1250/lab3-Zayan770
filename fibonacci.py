#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.
while True:
    num = input("Enter a positive integer: ")
    if num.isdigit() and int(num) > 0:  # Check if input is a positive integer
        num = int(num)
        break   
    else:
        print("Invalid input. Please enter a positive integer.")

a = 0
b = 1
for i in range(num):
    print(a, end=' ' if i < num - 1 else '')
    a, b = b, a + b
