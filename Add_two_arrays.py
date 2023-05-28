"""
Write a program to add the corresponding elements of two arrays, each of size $$N$$ and print the sums.
$$N$$ can be any integer between 1 and 100. $$1 \le N \le 100$$

Sample Input:
$$N$$ = 3
$$numArrayA$$ = 3 9 8
$$numArrayB$$ = 8 12 74

Sample Output:
11 21 82

"""

N = int(input("Enter the size of the arrays (N): "))

Arr1= list (map(int, input("Enter the list of numbers in array 1 seperated by spaces:    ").split()))
Arr2 = list (map(int, input("Enter the list of numbers in array 2 seperated by spaces:    ").split()))

sumArr = []

for i in range(0,N):
    sumArr.append(Arr1[i]+Arr2[i])

#Printing the sum array
for element in sumArr:
    print (element,end= "  ")