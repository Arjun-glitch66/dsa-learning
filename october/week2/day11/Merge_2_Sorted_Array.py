
def merge(list1,list2):
    m=len(list1)
    n=len(list2)
    result=[0]*(m+n)
    i=0
    j=0
    k=0
    while i<m and j<n:
        if list1[i]<=list2[j]:
            result[k]=list1[i]
            i+=1
        else:
            result[k]=list2[j]
            j+=1
        k+=1
    while i<m:
        result[k]=list1[i]
        i+=1
        k+=1
    while j<n:
        result[k]=list2[j]
        j+=1
        k+=1
    return result
list1=[1,2,4]
list2=[1,3,4]
print(merge(list1,list2))
