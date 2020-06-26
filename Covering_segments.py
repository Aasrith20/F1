n=int(input())
points=[]
for i in range(n):
  line_1=input()
  q=line_1.split()
  c=map(int,q)
  points.append(list(c))
points.sort(key=lambda x:x[1])
i=0
size=len(points)-1
ans=[]
while(points!=[]):
    i=0
    n=points[0][1]
    while(i<=size):
        q=0
        a=points[i][0]
        b=points[i][1]
        if n in range(a,b+1):
            points.remove(points[i])
            size=size-1
            i=0
            q=3
        if q==0:
            i=i+1
    ans.append(n)
print(len(ans))
print(" ".join(str(w) for w in ans))
