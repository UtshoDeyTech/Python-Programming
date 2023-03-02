s=input()
arr =[]
for i in s.split():
    arr.append(i)
a=float(arr[0])
b=float(arr[1])

s2=input()
arr2 =[]
for i in s2.split():
    arr2.append(i)
x=float(arr2[0])
y=float(arr2[1])

value=((a-x)**2+(b-y)**2)**(.5)
print('%.4f'%value)

