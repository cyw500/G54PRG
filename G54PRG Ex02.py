"Programming with Python (G54PRG) 2nd exercise"
x = low = -10
y = high = 10
print("Think of a number between {} and {}!".format(x,y))
count = 0
gotit = False
while not gotit:
    guess = (low + high) // 2

    print("Is your number greater (>), equal (=), or less (<) than {}?".format(guess))
    answer = input("Please answer <,=, or >! ")
   
    count += 1
    end = "I needed {} steps!".format(count)

    if answer == "=":
        print("I have guessed it!")
        gotit = True
        break
    elif answer == "<":
        high = guess
    elif answer == ">":
        if guess != y and guess == (y - 1):
            low = y
            continue
        else:
            low = guess
    else: # when user input is not ">" or "=" or "<"
        count -= 1
        print("Please answer with a single symbol of < or = or > only!")

    if low == high:
        if low == x or high == y :
            end = "You must be thinking outside the range, the number must between {} and {}!".format(x, y)
            break
        else:
            end = "What are you thinking? It is need to be a whole number!"
            break
    if (high - low) == 1:
        end = "What are you thinking? It is need to be a whole number!"
        break

print(end)
