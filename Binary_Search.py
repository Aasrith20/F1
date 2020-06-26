sorted=list(map(int,input().split()))
search=list(map(int,input().split()))
sorted.remove(sorted[0])
search.remove(search[0])
ans=[]
def binary_search(a, x):
    left, right = 0, len(a)-1
    while right-left>1:
        mid = (left + right) // 2
        if x<a[mid]:
            right=mid
        else:
            left = mid
    if sorted[right]==x:
        return(right)
    elif sorted[left]==x:
        return(left)
    return -1
for i in search:
  c=binary_search(sorted,i)
  ans.append(c)
print(" ".join(str(i) for i in ans))
"""def binary_search(sorted,x):
    left, right = 0, len(sorted)-1
    while right>=left:
        mid = left + right) // 2
        if x >sorted[mid]:
          left=mid+1
        elif x<sorted[mid]:
            right = mid-1
        else:
           return(mid)
    return(-1)"""
