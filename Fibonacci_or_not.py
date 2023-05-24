n=int(input())
a=0
b=1
cnt=0
for i in range(n):
    c=a+b
    if c==n:
        cnt+=1
        break
    else:
        a=b
        b=c
if cnt!=0:
    print("True")
else:
    print("False")