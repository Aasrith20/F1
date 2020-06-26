values=list(map(int,input().split()))
segments=[]
abcissa=[]
ordinate=[]
for i in range(values[0]):
    lol=list(map(int,input().split()))
    abcissa.append((lol[0],'l'))
    ordinate.append((lol[1],'r'))
val=list(map(int,input().split()))
var=[]
p=0
for i in val:
    var.append((i,"v"))
segments.extend(abcissa)
segments.extend(var)
segments.extend(ordinate)
segments.sort(key=lambda x:x[0])
seg=0
q=dict()
for i in segments:
    if i[1]=='l':
        seg+=1
    elif i[1]=='r':
        seg-=1
    else:
        q[i[0]]=seg
ans=[]
for i in val:
    ans.append(q[i])
print(" ".join(str(i) for i in ans))
