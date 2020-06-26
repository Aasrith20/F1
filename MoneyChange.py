n=int(input())
coins=[1,3,4]
ans=[0]*(n+1)
for i in range(1,n+1):
    min=float("inf")
    for p in coins:
     if i>=p:
       val=ans[i-p]+1
       if val<min:
         min=val
    ans[i]=min
print(ans[n])
