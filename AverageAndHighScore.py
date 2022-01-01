'''This program seeks to implement the basics of the sum and len functions.
The program will calculate the average height out of a list of numbers entered by the user'''

heights = input("Enter a list of random heights separated by  comma:\n").split(",")
result = 0
counter = 0
max_height = 0
for height in heights:
    result += float(height)
    counter += 1


for max in heights:
    if float(max) > max_height:
        max_height = float(max)
average_height = round((result / counter), 2)
print(f"The average height is {average_height}")
print(f"The max height is {max_height}")