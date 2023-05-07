r,c=map(int,input().split())
mat=[]
even=0
odd=0
for i in range(r):
    sub_list=list(map(int,input().split()))
    mat.append(sub_list)
for i in range(r):
    for j in range(c):
        if mat[i][j]%2==0:
            even=even+mat[i][j]
        else:
            odd=odd+mat[i][j]
print(even,odd)