n=int(input())
source=[0,0]
trace=[0,0]
for i in range(2,n+1):
    a,b,c=0,0,0
    w=i//3
    e=i//2
    #print(i,w,e)
    if i%2==0 and i%3==0:
        t=min(source[e],source[w],source[i-1])
        q=t+1
        source.append(q)
        a,b=1,1
        #print("first")
    elif i%2==0 and i%3!=0:
        t=min(source[e],source[i-1])
        q=t+1
        a=1
        source.append(q)
        #print("second")
    elif i%3==0 and i%2!=0:
        t=min(source[w],source[i-1])
        q=t+1
        b=1
        source.append(q)
        #print("third")
    else:
        t=source[i-1]
        source.append(source[i-1]+1)
        #print("fourth")
    if t==source[i-1] and i%1==0:
        #print(i,i-1,"third",sep="|")
        trace.append(i-1)
    elif t==source[w] and b==1 :
        #print(i,w,"second",sep="|")
        trace.append(w)
    else:
        #print(i,e,"first",sep="|")
        trace.append(e)
#print(list(enumerate(trace)))
#print(list(enumerate(source)))
print(source[n])
element=0
ans=[n]
if n>1:
    while(element!=1):
        element=trace[n]
        ans.append(element)
        n=element
    print(" ".join(str(i) for i in reversed(ans)))
else:
    print(1)
