'''
Secrete word
'''
secret_word = "qian"
guess = ""  # variable to store users' guess.
guess_count = 0
guess_limite = 3
out_of_guesses = False

while guess != secret_word and not out_of_guesses:
    if guess_count < guess_limite:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of guess, you lose!")
else:
    print("You win!")