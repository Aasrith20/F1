import numpy as np
n_1=int(input())
first=list(map(int,input().split()))
n_2=int(input())
second=list(map(int,input().split()))
n_3=int(input())
third=list(map(int,input().split()))
a=np.zeros((len(third)+1,len(first)+1,len(second)+1))
#print(a)
i,j,k=1,1,1
count=0
#print(first,second,third)
#print(a)

for p in range(1,len(third)+1):
    element=third[p-1]
    #print(element)
    for q in range(1,len(first)+1):
        for r in range(1,len(second)+1):
            #print(k,i,j,sep="||")
            if first[q-1]==element and second[r-1]==element:
                a[k][i][j]=a[k-1][i-1][j-1]+1
            else:
                a[k][i][j]=max(a[k][i-1][j],a[k-1][i][j],a[k][i][j-1])
            j+=1
        i+=1
        j=1
    j=1
    i=1
    k+=1
print(int(a[len(third)][len(first)][len(second)]))
