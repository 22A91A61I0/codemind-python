def prime(n):
    c=0
    for i in range(1,n+1):
        if(n%i==0):
            c=c+1
    if c==2:
        return True
    else:
        return False
a=int(input())
b=int(input())
for i in range(a,b+1):
    if prime(i)==True:
        print(i)