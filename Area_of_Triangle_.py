def area(a,b,c):
    s=(a+b+c)/2
    res=(s*(s-a)*(s-b)*(s-c))**0.5
    print('%.2f'%res)
a,b,c=map(int,input().split())
area(a,b,c)