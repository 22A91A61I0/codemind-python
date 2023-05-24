a=int(input())
b=a*a
c=a
p=0
s=0
while c!=0:
 r=c%10
 s=s*10+r
 c=c//10
d=s*s
while d!=0:
 q=d%10
 p=p*10+q
 d=d//10
if p==b:
   print("True")
else:
   print("False")