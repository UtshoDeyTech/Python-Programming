s=input()
arr =[]
for i in s.split():
    arr.append(i)
a=int(arr[0])
b=int(arr[1])
c=float(arr[2])

s2=input()
arr2 =[]
for i in s2.split():
    arr2.append(i)
x=int(arr2[0])
y=int(arr2[1])
z=float(arr2[2])


output=b*c+y*z
print('VALOR A PAGAR: R$ %.2f'%output)

