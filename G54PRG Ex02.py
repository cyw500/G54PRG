# Programming with Python (G54PRG) 2nd exercise"
cnt = 0  # Number of guesses made.
lower_bound = 1    # Minimum permissible user number.
upper_bound = 100  # Maximum permissible user number.

while True:
	# Make a guess at the user's number. The next number guessed will be midway between the largest and smallest possible numbers the user can be thinking of.
    guess = (lower_bound + upper_bound) // 2
    print("Is your number greater than (>), equal to (=), or less then (<) {}?".format(guess))
    answer = input("Please answer <, =, or >! ")
	# Update the bounds on the user's number, validate their guess and their input.

    cnt += 1
    if answer == "<": # The guess was too high.
        if guess == lower_bound:
            print("Sorry, the number you're thinking of is an illegitimate number!")
            break
        upper_bound = guess - 1
    elif answer == ">":  # The guess was too low.
        if guess == upper_bound:
            print("Sorry, the number you're thinking of is an illegitimate number!")
            break
        lower_bound = guess + 1
    elif answer == "=":  # The guess was correct.
        print("I have guessed it! \nI needed {} steps!".format(cnt))
        break
    else:  # The user's input wasn't valid (i.e. It wasn't equal to <, = or > )
        cnt -= 1
        print("Please answer with the symbol <, = or > only!")