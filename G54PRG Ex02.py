"Programming with Python (G54PRG) 2nd exercise"
low = 1
high = 100
print("Think of a number between {} and {}!".format(low,high))
count = 0
Gotit = False
while not Gotit:
    guess =(low+high)//2

    print ("Is your number greater (>), equal (=), or less (<) than {}?".format(guess))    
    answer = input("Please answer <,=, or >! ")
   
    count += 1
    if answer == "=":
        print ("I have guessed it!")
        Gotit = True
    elif answer == "<":
        high = guess
    elif answer == ">": 
        low = guess
    else: # when user input did is not ">" or "=" or "<"
        count -= 1
        print ( "Please answer with a single symbol of < or = or > only!")

print("I needed {} steps!".format(count))
