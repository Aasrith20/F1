#Does not pass for 100000
n=int(input())
a=[0,0]
b=[0,0]
for i in range(2,n+1):
    w=int(i/3)
    e=int(i/2)
    #print(i,w,e)
    if i%2==0 and i%3==0:
        t=min(a[e],a[w],a[i-1])
        q=t+1
        a.append(q)
        #print("first")
    elif i%2==0 and i%3!=0:
        t=min(a[e],a[i-1])
        q=t+1
        a.append(q)
        #print("second")
    elif i%3==0x and i%2!=0:
        t=min(a[w],a[i-1])
        q=t+1
        a.append(q)
        #print("third")
    else:
        t=a[i-1]
        a.append(a[i-1]+1)
        #print("fourth")
    if t==a[i-1]:
        #print(i,i-1,"third",sep="|")
        b.append(i-1)
    elif t==a[w]:
        #print(i,w,"second",sep="|")
        b.append(w)
    else:
        #print(i,e,"first",sep="|")
        b.append(e)
print(list(enumerate(b)))
#print(list(enumerate(a)))
print(a[n])
element=0
ans=[n]
if n>1:
    while(element!=1):
        element=b[n]
        ans.append(element)
        n=element
    print(" ".join(str(i) for i in reversed(ans)))
