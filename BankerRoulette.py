import random
names_string = input("Give me everybody's names, separated by a comma.\n")
names = names_string.split(", ")
counter = random.randint(0, len(names)-1)

print(f"{names[counter]} will pay the bill today")

##############you can use the choice function to select from a list ####################
#print(f"{random.choice(names)} will pay the bill today")
#####################################