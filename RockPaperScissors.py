import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_options = [rock, paper, scissors]
user_input = int(input("What do you choose?\n Enter 0 for rock, 1 for paper, and 2 for scissors\n"))
pc_input = game_options.index(random.choice(game_options))

print(f"You selected {user_input}\n{game_options[user_input]}")
print("")
print(f"PC selected {pc_input}\n{game_options[pc_input]}")

if user_input >= 3 or user_input < 0: 
  print("You typed an invalid number, you lose!") 
elif user_input == 0 and pc_input == 2:
  print("You win!")
elif pc_input == 0 and user_input == 2:
  print("You lose")
elif pc_input > user_input:
  print("You lose")
elif user_input > pc_input:
  print("You win!")
elif pc_input == user_input:
  print("It's a draw")
