import random
dictionary = open("hangman_wordlist.txt", "r")
read_dictionary = dictionary. readlines()
wordlist = []
game_word = ""
len_of_gameword = int(input("What should be the minimum length for words?:\n"))

for word in read_dictionary:
    if len(word) >= len_of_gameword:
        wordlist.append(word.replace("\n", ""))

gameword = random.choice(wordlist)
blanks = "_ "
print(blanks * len_of_gameword)
