n=int(input())
a=list(map(int,input().split()))
a.sort()
w=0
search=None
for i in a:
    if i!=search:
        count=0
        search=i
    if search==i:
        count+=1
        if count>len(a)/2:
            print(1)
            w=1
            break
if w==0:
    print(0)
