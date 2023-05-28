# Write a program to list all the integers between two integers L and R (including L and R).
# L and R can be any integer between 1 and 100. 1≤L,R≤100

"""
Sample Input:
L = 5, R = 10
Sample Output:
5 6 7 8 9 10
"""


L, R  = map(int, input("Enter the values of L and R separated by a space: ").split())

for i in range(L, R+1):
    print(i, end=" ")
    