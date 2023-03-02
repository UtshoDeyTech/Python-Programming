a=1
j=7
while(a<10):
    for x in range(3):
        print("I=%d J=%d" %(a,j))
        j+=-1
    a+=2
    j=a+6