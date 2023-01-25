import random

word_list = ["Apple", "Banana", "Watermelon", "Pomegranate", "Melon"]
print(word_list)

word = random.choice(word_list)

print(word)

guess = input('Please enter 1 letter')

if len(guess) == 1 and guess.isalpha() == True:
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
