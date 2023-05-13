import random 

game = input (" do you  wish to play a number guessing game? Type yes or no ?").lower()
if game=="yes":
    print ("okay ! lets move on ")
elif game== "no":
    print ("Sorry to hear that")
    quit()

x = input ("Type a number: ")
print (" Clue: The random number which you should guess resides in between your input number and zero ")

if x.isdigit():
    x = int (x)

    if x <= 0 :
        print ("Please type a number larger than 0 next time.")
        quit ()
    
else:
     print('Please type a number next time.')
     quit()


random_number =random.randint(0,x)
guesses = 0

while True:
    guesses = guesses +1
    user_guess = input ("Make a guess:" )
    if user_guess.isdigit():
        user_guess= int(user_guess)
    else:
         print('Please type a number next time.')
         continue
    
    if user_guess == random_number:
        print ("you got it!")
        break
    elif user_guess>random_number:
        print ("You were above the number!")
    else:
          print("You were below the number!")


print("You got it in", guesses, "guesses")





       

