

def merge(nums1,m,nums2,n):
    merged=[0]*(m+n)
    i=0
    j=0
    k=0
    while i<m and j<n:
        if nums1[i]<=nums2[j]:
            merged[k]=nums1[i]
            i+=1
        else:
            merged[k]=nums2[j]
            j+=1
        k+=1
    while i<m:
        merged[k]=nums1[i]
        i+=1
        k+=1
    while j<n:
        merged[k]=nums2[j]
        j+=1
        k+=1
    for k in range(m+n):
        nums1[k]=merged[k]
nums1=[1,2,3,0,0,0]
nums2=[2,5,6]
merge(nums1,3,nums2,3)
print(nums1)
