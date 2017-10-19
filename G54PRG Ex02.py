"Programming with Python (G54PRG) 2nd exercise"
bottom = low = 1
top = high = 100
<<<<<<< HEAD
n = math.log(top - bottom , 2)
print("OK I will show you a magic that I can guess what you thinking in less then {} steps if you thinking of a number between {} and {}!".format(math.ceil(n)+1, bottom,top))
=======
print("Think of a number between {} and {}!".format(bottom,top))
>>>>>>> parent of 2183a77... 1st
count = 0
while True:
    guess = (low + high) // 2

    print("Is your number greater (>), equal (=), or less (<) than {}?".format(guess))
    answer = input("Please answer <,=, or >! ")
   
    count += 1
    end = "I needed {} steps!".format(count)

    if answer == "=":
        print("I have guessed it!")
        break
    elif answer == "<":
        if guess != bottom and guess == (bottom + 1):
            high = bottom
            continue
        else:
            high = guess
    elif answer == ">":
        if guess != top and guess == (top - 1):
            low = top
            continue
        else:
            low = guess
    else: # when user input is not ">" or "=" or "<"
        count -= 1
        print("Please answer with a single symbol of < or = or > only!")
    #    continue

    if low == high:
        end = "you must be thinking outside the range, the number must between {} and {}!".format(bottom , top)
        break
    if (high - low) == 1:
        end = "What are you thinking? It is need to be a whole number!"
        break

print(end)