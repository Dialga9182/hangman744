import random

word_list = ['apple', 'banana', 'cherry', 'dragonfruit', 'elderberry']

class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word = random.choice(word_list) # The word to be guessed, picked randomly from the word_list.
        self.word_guessed = ['_'] * len(self.word)# A list of '_'s, the number of which is the len(self.word)
        self.num_letters = len(list(set(self.word))) # Length of the list of the unique letters in word.
        '''#The number of UNIQUE letters in the word that have not been guessed yet.
        #Two conditions
        #1: the letters have to have not been guessed yet, so still '_'s.
        #2: the letters must be unique.
        
        #First idea:
        #testing the limits of isalpha.
            #txt = '_'
            #x = txt.isalpha()
            #print(x) # False
        #testing the limits of isalpha.
        #learned that _ is going to be not considered the same as a, or b, or c etc...
        #so can distinguish between alphabeticals and _s.
        #question: can I count the number of '_'s in a list?
        #it will have to involve checking if each element of a list isalpha'''
        self.num_lives = num_lives # Number of lives at the start.
        self.word_list = word_list # The list of words.
        self.list_of_guesses = [] # A list of the guesses that have already been tried.
    
    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word")
        #else
        
    def ask_for_input(self):
        while True:
            guess = input("Please enter a single letter: ")
            if len(guess) != 1 or guess.isalpha() != True:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
                
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                print(self.list_of_guesses)

my_hangman_instance = Hangman(word_list)
my_hangman_instance.ask_for_input()