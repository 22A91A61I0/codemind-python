n=int(input())
arr=list(map(int,input().split()))
maxi=len(str(arr[0]))
c=1
for i in arr[1:]:
    num=len(str(i))
    if num>maxi:
        maxi=num
        c=1
    elif num==maxi:
        c+=1
print(c)