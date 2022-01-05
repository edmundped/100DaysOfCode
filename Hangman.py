import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

dictionary = open("hangman_wordlist.txt", "r")
read_dictionary = dictionary. readlines()
wordlist = []
blanks = []
lives = 6
len_of_gameword = int(input("What should be the minimum length for words?:\n"))

for word in read_dictionary:
    if len(word) >= len_of_gameword:
        wordlist.append(word.replace("\n", ""))

gameword = random.choice(wordlist)

for blank in range(len(gameword)):
    blanks += "_"



end_of_game = False

while not end_of_game:
    guess_letter = input("Guess a letter:").lower()
    for position in range(len(gameword)):
        letter = gameword[position]
        if letter == guess_letter:
            blanks[position] = letter

    #print(blanks)

    if guess_letter not in gameword:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose!")

    print(f"".join(blanks))

    if "_" not in blanks:
        end_of_game = True
        print("You win!")

    print(stages[lives])

