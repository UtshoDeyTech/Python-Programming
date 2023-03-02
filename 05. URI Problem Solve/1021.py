s=[100,50,20,10,5,2,1,0.50,0.25,0.10,0.05,0.01]
n=float(input())
for i in s:
    x=n//i
    n=n%i
    if i>1:
        if i==100:
            print('NOTAS:')
        print(int(x),'nota(s) de R$','%.2f'%i)
    else:
        if i==1:
            print('MOEDAS:')
        print(int(x),'moeda(s) de R$','%.2f'%i)