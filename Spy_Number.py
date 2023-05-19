n=int(input())
sum=0
p=1
while n!=0:
    r=n%10
    sum+=r
    p=p*r
    n//=10
if sum==p:
    print("Spy Number")
else:
    print("Not Spy Number")