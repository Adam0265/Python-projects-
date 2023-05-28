def factorial(n):
    if n == 1 or n == 0 :
        return 1
    else:
        return  n*factorial(n-1)

sample = int(input("Enter the number: "))
print (factorial(sample))