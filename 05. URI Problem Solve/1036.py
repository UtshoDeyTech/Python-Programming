s=input()
arr=[]
for i in s.split():
    arr.append(i)
a=float(arr[0])
b=float(arr[1])
c=float(arr[2])

m=(b*b)-(4*a*c)
if m<0 or a==0:
    print('Impossivel calcular')
else:
    n=((-b) + (m)**0.5)/(a+a)
    p=((-b) - (m)**0.5)/(a+a)
    print('R1 = %.5f'%n)
    print('R2 = %.5f'%p)