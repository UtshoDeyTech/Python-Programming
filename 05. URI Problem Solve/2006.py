x=int(input())
s=input()
arr =[]
for i in s.split():
    i=int(i)
    arr.append(i)
print(arr.count(x))

