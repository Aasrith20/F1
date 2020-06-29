import numpy as np
first=input()
second=input()
b=[[0]*(len(first)+1)]*(len(second)+1)
a=np.array(b)
count=0
for i in range(len(first)+1):
    a[0][i]=count
    count+=1
count=0
for i in range(len(second)+1):
    a[i][0]=count
    count+=1
i,j=1,1
#print(second,len(second),first,len(first))
for p in first:
    for q in second:
        if p==q:
            a[i][j]=a[i-1][j-1]
        if p!=q:
            #print(a[i-1][j-1],a[i-1][j],a[i][j-1],i,j)
            a[i][j]=min(a[i-1][j-1],a[i-1][j],a[i][j-1])+1
        #print(a)
        i+=1
    j+=1
    i=1
print(a[len(second)][len(first)])
