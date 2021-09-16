'''
# Things that will be used ["variable",  "Loops",  "if-statements"]
# In other to build the game 
# keep guessing
we will prompt the user to enter the secret word
'''

secret_word = "Ibraheem"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False


while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of guesses, YOU LOSE!")
else:
    print("You win!")