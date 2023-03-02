x=int(input())
if x%2:
    for i in range(x,x+11,2):
        print(i)
else:
    for i in range(x+1,x+12,2):
        print(i)