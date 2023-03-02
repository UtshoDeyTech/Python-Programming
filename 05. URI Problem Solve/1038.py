s=input()
arr =[]
for i in s.split():
    arr.append(i)
a=int(arr[0])
b=int(arr[1])
if a==1:
    b=b*4.00
elif a==2:
    b=b*4.50
elif a==3:
    b=b*5.00
elif a==4:
    b=b*2.00
elif a==5:
    b=b*1.50
print('Total: R$ %.2f'%b)
