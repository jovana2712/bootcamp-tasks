import random

"""
The function written below plays a game with the user by generating a random number between 1 and 100. The user is supposed
to guess the number and with each guess, the code will provide feedback: if the user guessed a number that is lower than 
the actual random one, the code will output "higher" to indicate that the next guess should be higher and that the 
generated number is higher. The same logic is applied if the user guesses a number that is higher than the generated one.
If the user successfully guesses the random number, the code will provide output saying that the number has been guessed
correctly. 
To know whether the user guessed a higher/lower value, we use specific values as indicators that will help us determine
the output that will be provided to the user. After we compare the guessed value and the randomly generated number, we assign
numeric values such as -1,0,1 or 2 to a variable that will later help us determine in which direction should the user move 
further. 
If, for example, the actual number is 10 and the user guessed 7, we know that 7<10 and we can assign value -1 to the variable var. 
Later, when we check for the value of var, we will know that if its value is -1, the user should try to guess for a higher 
value than 7. Then, we will provide the output "higher" to tell the user that the value is higher than 7.
"""


def guess():
    """
    Generates a random integer using randint function from random and expects a user input to validate and check if the
    user has guessed the number correctly or not. If the user has guessed a smaller number than the generated one, the
    code will output "higher" to indicate that the number is higher than the guessed one. If the user has guessed a larger
    number than the generated one the code will output "lower" to indicate that the number is lower than the guessed one.
    Finally, if the user guesses the number correctly, the code will output "Correct! Well done!"
    """
    # Generating a random number between 1 and 100
    result = random.randint(1, 100)
    print("Guess the number between 1 and 100!")
    # Initialise the value of guess as None, as it has no starting value
    guess = None

    # Loop through all guesses from user until the user guesses the one that matches the random number
    while guess != result:
        # Take the input from the user
        guess = input()
        # Perform checking of the value in a separate function - gives us a more neat and clear code
        val = check(guess, result)
        # Prints the response according to the value that is obtained from "check" function
        print_response(val)


def check(guess, result):
    """
    Checks whether the guess that we obtained from user matches the randomly generated number. If it does, the function
    returns 0. If the number is not in the range, i.e. not between 1 and 100, we return a value 2. If the guessed value
    is smaller than the generated number, return -1. If the guessed number if larger than the generated one, return 1.
    :param guess: the guessed number from the user
    :param result: the generated random number
    :return: an integer value that will be used in the function that prints the response (-1,0,1 or 2)
    """
    # We convert the number to integer, as since it has been obtained from the command line, it is a type of String
    # Note that we cannot perform comparisons between Strings and integers, which is why we cast the guess to integer type
    guess = int(guess)

    # Check if the guessed value is in the range
    if guess < 1 or guess > 100:
        return 2
    # Check if the guessed value is smaller than the generated random number
    elif guess < result:
        return -1
    # Check if the guessed value is larger than the generated random number
    elif guess > result:
        return 1
    # The value equals to the generated random number
    else:
        return 0


def print_response(checked_val):
    """
    Prints the response to the user based on the value that is obtained from function that compares the guessed number
    and randomly generated number. This gives the user an indication of what their next guess should be and how close to
    guessing the correct number are.
    :param checked_val: value obtained from "check" function
    """
    # If the guessed number was lower than the random generated one, the user should try going higher
    if checked_val == -1:
        print("Higher")
    # If the guessed number was higher than the random generated one, the user should try going lower
    elif checked_val == 1:
        print("Lower")
    # If the guessed number wasn't in the correct range (1-100)
    elif checked_val == 2:
        print("Value not in the range! Please try a number between 1 and 100!")
    # If the number was guessed correctly
    else:
        print("Correct! Well done!")


guess()
