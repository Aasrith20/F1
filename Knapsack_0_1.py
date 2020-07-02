import numpy as np 
line=list(map(int,input().split()))
values=list(map(int,input().split()))
weights=[]
weights.extend(values)
a=[[0]*(line[0]+1)]*(line[1]+1)
a=np.array(a)
#print(a)
for i in range(1,line[1]+1):
   # print(a)
    for j in range(1,line[0]+1):
        if weights[i-1]<=j:
            a[i][j]=max(values[i-1]+a[i-1][j-weights[i-1]],a[i-1][j])
        else:
            a[i][j]=a[i-1][j]
#print(a)
print(a[line[1]][line[0]])
