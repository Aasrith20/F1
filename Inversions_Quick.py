n=int(input())
a=list(map(int,input().split()))
#Count if the next consecutive element is less than the element you are working on!!
#[2,3,9,2,9] here 3>2 count=1; and 9>2 count=2;
#[2,3,9][2,9] here 3>2 so the elements after 3 are also greater than 2 cause the list is sorted thus 3,9 both are greater than 2 so number of inversions is 2
lower=0
upper=n-1
def Division(a,lower,upper,R):
 #print("Splitting:"+str((a[lower:upper+1])))
 if upper>lower:
    mid=(lower+upper)//2
    A=Division(a,lower,mid,R)
    B=Division(a,mid+1,upper,R)
 else:
     return(a[lower:upper+1])
 #print("Merging:"+str(A)+str(B))
 C=Merge(A,B,R)
 #print(str(C))
 return(C)
def Merge(A,B,R):
    c=[]
    a=0
    b=0
    while(True):
       if a==len(A):
           c.extend(B[b:])
           break
       if b==len(B):
           c.extend(A[a:])
           break
       if A[a]<=B[b]:
           c.append(A[a])
           a=a+1
       else:
           c.append(B[b])
           R[0]=R[0]+(len(A)-a)
           b=b+1;
    return(c)
R=[0]
q=Division(a,0,upper,R)
print(R[0])
