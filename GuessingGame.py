'''Question 3: The Guessing Game
Create a number guessing game. Set a secret number (e.g., 42). Allow the user a maximum of 5 attempts to guess it
using a while loop.
If they enter a number less than 1 or greater than 100, use continue to skip the attempt without counting it.
If they guess correctly, print a success message and break the loop.
Use the else block with the while loop to print "Game Over! You lost." if they run out of attempts.'''


secret = 42
attempts = 0

while attempts < 5:
    number = int(input("Guess the secret number: "))
    if number < 1 or number > 100:
        print("Invalid number.")
        continue
    attempts += 1
    if number == secret:
        print("You WIN!")
        break
    else:
        print("Try again.")

else:
    print("Game Over! You lost.")
