import random
word_list = ['apple', 'banana', 'cherry', 'dragonfruit', 'elderberry']
word = random.choice(word_list)

guess = input("Please enter a single letter: ")
if len(guess) == 1 and guess.isalpha() == True:
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")