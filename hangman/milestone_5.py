import random

word_list = ['apple', 'banana', 'cherry', 'dragonfruit', 'elderberry']

class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.
    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_of_guesses: list
        A list of the letters that have already been tried
    
    Methods:
    -------
    check_guess(guess)
        Checks if the letter is in the word.
    ask_for_input()
        Asks the user for a letter.
    '''
    def __init__(self, word_list, num_lives = 5):
        self.word = random.choice(word_list) # The word to be guessed, picked randomly from the word_list.
        self.word_guessed = ['_'] * len(self.word)# A list of '_'s, the number of which is the len(self.word)
        self.num_letters = len(list(set(self.word))) # Length of the list of the unique letters in word.
        self.num_lives = num_lives # Number of lives at the start.
        self.word_list = word_list # The list of words.
        self.list_of_guesses = [] # A list of the guesses that have already been tried.
    
    def check_guess(self, guess):
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.
        
        Parameters:
        ----------
        guess: str
            The letter to be checked
        '''
        guess = guess.lower() # Ensures guess is lowercase.
        indices = [i for i, x in enumerate(self.word) if x == guess] # list of indices where guess in word.
        lst_of_replacement_strings = [guess] * self.word.count(guess) # list of strings, all are guess.
        if guess in self.word: # If guess can be found in word then.
            print(f"Good guess! {guess} is in the word")
            for letter in self.word: #for each letter in the random word picked
                if letter == guess: #check if the letter is the one guessed
                    for x,y in zip(indices,lst_of_replacement_strings): # Loop over x and y, feed in params.
                    #for x element in indices, and for y element in lst_of...
                        self.word_guessed[x] = y # Replaces element at an index x, with y
                    #replace element stored at x index of self.word_guessed with element
                    #stored at y in lst_of...
            #print(self.num_letters)
            self.num_letters -=1
            #print(self.num_letters)
            print(self.word_guessed)
        else:
            self.num_lives -=1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
        
    def ask_for_input(self):
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method.
        '''
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
                break

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        #print(game.num_lives)
        #print(game.num_letters)
        if game.num_lives == 0 or game.num_lives < 0:
            print("You lost!")
            break
        if game.num_lives != 0 and not game.num_letters > 0:
            print("Congratulations. You won the game!")
            break
        if game.num_letters >= 1:
            game.ask_for_input()
    return 5+5
            
if __name__ == '__main__':
    word_list = ['apple', 'banana', 'cherry', 'dragonfruit', 'elderberry']
    play_game(word_list)