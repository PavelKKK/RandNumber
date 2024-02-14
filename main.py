import random  # Import module random

max_attempts = 3  # Add the number of attempts to enter
attempts = 0  # Initial number of attempts

while attempts < max_attempts:
    randomNumber = random.randint(1, 50)  # We generate numbers from 1 to 50 and integers

    try:
        userNum = int(input("Enter a number from 1 to 50:"))  # Requesting input from the user
        if userNum == randomNumber:
            print("Correct")
            print("It's my number:", randomNumber)
        elif userNum != randomNumber:
            print("Not correct")
            print("It's my number:", randomNumber)
            attempts += 1  # Adding attempts when entering a number incorrectly
        continue
    except ValueError:
        print("Error! Enter an integer.")
        attempts += 1

if attempts == max_attempts:  # And if the number of attempts is exhausted, then the cycle stops
    print('Attempt limit exceeded')
