count = 0
bottom = 1
top = 100

while True:
    guess = (top + bottom) // 2
    print("Is your number greater (>), equal (=), or less (<) than {}?".format(guess))
    answer = input("Please answer <,=, or >! ")

    count += 1
    if answer == "<":
        if guess == bottom:
            print("Sorry, the number you thinking is an illegitimate number!")
            break
        top = guess - 1
    elif answer == ">":
        if guess == top:
            print("Sorry, the number you thinking is an illegitimate number!")
            break
        bottom = guess + 1
    elif answer == "=":
        print("I have guessed it! \nI needed {} steps!".format(count))
        break
    else: # if input is not equal to < or = or >
        count -= 1
        print("Please answer with the symbol of < or = or > only!")