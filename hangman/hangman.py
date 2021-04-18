# Program ID: hangman
# Author: Courtney Ng & Jasmine Li
# Period: 7
# Program Description: Using the character split to create hangman game
# This Part we just don't get it

# Variables
yes = "yes"
no = "no"
guessedList = []

# Executioner
word = input("Enter a word")
charList = list(word) # makes each letter own element
length = len(word)

# My failed attempts.

# for x in range(0,len(charList)):
#    print("_")

            # for char in word:
             #   if char in guess:
              #      print(char)
               # else:
                #    print("_")

                 # if guess == word[i]:
            #    if charList == guess:
            #         guessedList[x] == guess
# def Guess():
#     guesses = 1

#     while guesses < 7:
# Start

ans = input("Do you want to play hangman?")
while ans == yes:
    for char in word:
        guessedList.append("_")
    guess = input("Insert a letter")
    guessedList.append(guess)
    if guess in charList:
        for x in range(0, len(word)):
            if word[x] == guess:
                guessedList[x] = guess
                print(guessedList)
    else:
        if char not in word:
            guessedList.append("_")
            print(guessedList)