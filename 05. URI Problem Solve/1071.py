x=int(input())
y=int(input())
m=0
if(x>y):
    for i in range(y+1,x,1):
        if i%2==1:
            m=m+i
else:
    for i in range(x+1,y,1):
        if i%2==1:
            m=m+i
print(m)