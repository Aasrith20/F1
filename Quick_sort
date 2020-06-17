n=input()
array=list(map(int,input().split()))
def Loop(array,lower,upper):
    if(lower<upper):
        left_upper,right_lower=QuickSort(array,lower,upper)
        Loop(array,lower,left_upper)
        Loop(array,right_lower,upper)
def QuickSort(array,lower,upper):
    q=lower
    index=lower
    pivot=array[upper]
    for w in range(upper-lower):
        if array[index]<pivot:
            array[index],array[q]=array[q],array[index]
            q=q+1
        index=index+1
    array[upper],array[q]=array[q],pivot
    left_upper=q-1
    index=q+1
    q=q+1
    for w in range(upper-q+1):
        if array[index]==pivot:
            array[index],array[q]=array[q],array[index]
            q=q+1
        index=index+1
    right_upper=q
    return(left_upper,right_upper)
Loop(array,0,len(array)-1)
print(" ".join(str(i) for i in array))
