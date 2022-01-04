import random
dictionary = open("hangman_wordlist.txt", "r")
wordlist = dictionary. readlines()
game_word = ""
for word in wordlist:
    if len(word) >= int(input("What should be the minimum length for words?:\n")):
        game_word = random.choice(wordlist)

print(game_word)