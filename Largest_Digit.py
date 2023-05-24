def find(num):
    I=0
    while num>0:
        d=num%10
        if d>I:
            I=d
        num//=10
    return I
num=int(input())
largest=find(num)
print(largest)