#Take an input from the user
number = int (input("enter a numberto check : "))

if number > 1:
    for i in range (2,number):
        if number % i ==0:
            print ("its not a prime ")
    else:
        print (number , "It's a prime ") 

else:
    print ("Its not a prime ")
