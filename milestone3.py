from milestone2 import get_random_word


random_word = get_random_word().lower()

def check_guess(g):
    
    print(f"The word is {random_word}")
    
    if g in random_word:
        print(f"Good guess! {g} is in the word")
    else:
        print(f"Sorry, {g} is not in the word. Try again.")



def ask_for_input():

    while True:
        guess = input("Please enter a single letter: ")

        if len(guess) == 1 and guess.isalpha() == True:
            guess_lower_case = guess.lower()
            checked_guess = check_guess(guess_lower_case)
            return guess_lower_case

            break

        else:
            print("Invalid letter. Please, enter a single alphabetical character")

    

ask_for_input()
