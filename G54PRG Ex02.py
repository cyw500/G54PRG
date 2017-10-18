"Programming with Python (G54PRG) 2nd exercise"
x = low = 1
y = high = 100
print("Think of a number between {} and {}!".format(x,y))
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
    else: # when user input is not ">" or "=" or "<"
        count -= 1
        print ( "Please answer with a single symbol of < or = or > only!")
    if low == high :
        print ("You must be thinking outside the range, the number must between {} and {}!".format(x,y))

        ''' 
        thinking of asking do you want to try again but then I dont know how to feed it back to the loop again 
        (also if not how to not showing the "I needed ? steps!", I have consider putting if statement if count > 6 
        but it is possible to have 7 step to guess as well as it fall out of range)
        '''

        break
    elif guess == high - 1 :
        low += 1

print("I needed {} steps!".format(count))
