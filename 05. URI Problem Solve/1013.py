s=input()
arr =[]
for i in s.split():
    arr.append(i)
a=int(arr[0])
b=int(arr[1])
c=int(arr[2])

x=max(a,b,c)
print(x,'eh o maior')