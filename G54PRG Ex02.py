"Programming with Python (G54PRG) 2nd exercise"
bottom = low = 1
top = high = 100
print("Think of a number between {} and {}!".format(bottom,top))
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
        continue

    if low == high:
        if low == bottom or high == top :
            end = "you must be thinking outside the range, the number must between {} and {}!".format(bottom , top)
        else:
            end = "What are you thinking? It is need to be a whole number!"
        break
    if (high - low) == 1:
        end = "What are you thinking? It is need to be a whole number!"
        break

print(end)