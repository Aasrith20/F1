import math
n=int(input())
segments=[]
for i in range(n):
    lol=list(map(int,input().split()))
    segments.append(lol)
def dist(a,b):
    d=math.sqrt((b[0]-a[0])**2+(b[1]-a[1])**2)
    return(d)
def min_dist(a):
    min=float("inf")
    for i in range(len(a)-1):
        index=i+1
        for j in range(index,len(a)):
            c=dist(a[i],a[j])
            if c<min:
                min=c
            index=index+1
    return(min)
def Final(a,d):
    min=float("inf")
    for i in range(len(a)-1):
        index=i+1
        for j in range(index,len(a)):
            if a[j][1]-a[i][1]<=d:
               c=dist(a[i],a[j])
               if c<min:
                   min=c
            else:
                break
            index=index+1
    return(min)
def Merge(segments,n):
    if len(segments)<=3:
        return(min_dist(segments))
    mid=n//2
    x=segments[mid]
    da=Merge(segments[:mid],mid)
    db=Merge(segments[mid:],len(segments)-mid)
    d=min(da,db)
    strip=[]
    a=[i for i in segments[:mid] if abs(x[0]-i[0])<=abs(d)]
    b=[i for i in segments[mid:] if abs(i[0]-x[0])<=abs(d)]
    strip.extend(a)
    strip.extend(b)
    strip.sort(key=lambda x:x[1])
    return(min(d,Final(strip,d)))
segments.sort()
p=Merge(segments,len(segments))
print(round(p,3))

