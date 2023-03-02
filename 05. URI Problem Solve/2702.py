a= [int(x) for x in input().split()]
b= [int(x) for x in input().split()]
i=0
for x in range(3):
    j = b[x] - a[x]
    if j > 0:
        i += j

print(i)