n=int(input())
a=n*n
sum=0
while a!=0:
    r=a%10
    sum+=r
    a//=10
if sum==n:
    print("Neon Number")
else:
    print("Not Neon Number")