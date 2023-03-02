s=input()
arr=[]
for i in s.split():
    arr.append(i)
a=int(arr[0])
b=int(arr[1])
c=int(arr[2])
d=int(arr[3])
if (b>c and d>a) and (c+d>a+b) and (c>0 and d>0) and (a%2==0):
    print('Valores aceitos')
else:
    print('Valores nao aceitos')

