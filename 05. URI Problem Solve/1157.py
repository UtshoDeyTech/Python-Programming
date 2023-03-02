x=int(input())
for i in reversed(range(1,x+1,1)):
    if x%i==0:
        print(x//i)