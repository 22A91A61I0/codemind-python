n=int(input())
arr=list(map(int,input().split()))
mini=len(str(arr[0]))
c=1
for i in arr[1:]:
    num=len(str(i))
    if num<mini:
        mini=num
        c=1
    elif num==mini:
        c+=1
print(c)