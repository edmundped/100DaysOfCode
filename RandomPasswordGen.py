import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password = []

print("Welcome to the Random Password Generator!")
no_letters= int(input("How many letters would you like in your password?\n")) 
no_symbols = int(input(f"How many symbols would you like?\n"))
no_numbers = int(input(f"How many numbers would you like?\n"))

for letter in range(no_letters):
    password.append(random.choice(letters))

for letter in range(no_symbols):
    password.append(random.choice(symbols))

for letter in range(no_numbers):
    password.append(random.choice(numbers))

#print(password)
# the shuffle function returns None, and not the modified data. i.e implement like so;
# print(password)
# random.shuffle(password)
# print(password)
# this will shuffle the list
# you can use the sample function as implemented below
print(f"""Your password is:\n {"".join(random.sample(password, len(password)))}""")


