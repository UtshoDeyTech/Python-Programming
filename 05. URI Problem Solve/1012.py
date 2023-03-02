s=input()
arr =[]
for i in s.split():
    arr.append(i)
a=float(arr[0])
b=float(arr[1])
c=float(arr[2])

print('TRIANGULO: %.3f'%(.5*a*c))
print('CIRCULO: %.3f'%(3.14159*c*c))
print('TRAPEZIO: %.3f'%(.5*(a+b)*c))
print('QUADRADO: %.3f'%(b*b))
print('RETANGULO: %.3f'%(a*b))