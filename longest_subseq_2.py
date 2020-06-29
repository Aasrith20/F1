import numpy as np
n_1=int(input())
first=list(map(int,input().split()))
n_2=int(input())
second=list(map(int,input().split()))
b=[[0]*(len(first)+1)]*(len(second)+1)
a=np.array(b)
count=0
for i in range(len(first)+1):
    a[0][i]=0
    count+=1
count=0
for i in range(len(second)+1):
    a[i][0]=0
    count+=1
i,j=1,1
count=0
#print(second,len(second),first,len(first))
for p in first:
    for q in second:
        if p==q:
            a[i][j]=a[i-1][j-1]+1
        if p!=q:
            #print(a[i-1][j-1],a[i-1][j],a[i][j-1],i,j)
            a[i][j]=max(a[i-1][j],a[i][j-1])
        #print(a)
        i+=1
    j+=1
    i=1
print(a[len(second)][len(first)])
