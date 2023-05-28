lowest_num=float("inf")

arr = [10,1,2000,50000,6,4]

for i in arr:
    if i < lowest_num:
        lowest_num = i

print (lowest_num)