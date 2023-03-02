x=int(input())
m=0
for i in range(1,x+1,1):
    a,b=input().split()
    m=m+int(a)*int(b)
print(m)