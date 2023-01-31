
import random

class Hangman:

    def __init__(self,word_list,num_lives = 5):
        self.word = random.choice(word_list).lower()
        self.word_list = word_list
        self.num_lives = num_lives
        self.list_of_guesses = []
        self.num_letters = len(set(self.word))
        self.word_guessed = ["_"] * len(self.word)

    
    def check_guess(self, guess):
        lower_guess =  guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for index, elem in enumerate(self.word):
                if elem == guess:
                    self.word_guessed[index] = guess
            print(self.word_guessed)
            if "_" not in self.word_guessed:
                print("You won")
                exit()
            self.num_letters -= 1

        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left")
            if self.num_lives == 0:
                print("You lost")
        




    def ask_for_input(self):
        while True:
            guess = input("Please enter a single character as a guess: ")
            if len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You've already tried that letter")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

game = Hangman(['banana','apple','rasberry','pineapple','watermelon'])
game.ask_for_input()





