#2 pointer approach for removing duplicates
#sorted array
nums=[1,2,1,1,3,2]
sorted=sorted(nums)
print(sorted) #[1,1,1,2,2,3]
def check():
    left=0
    for right in range(1,len(sorted)):
        if sorted[left]==sorted[right]:
            continue
        else:
            left+=1
            temp=sorted[right]
            sorted[right]=sorted[left]
            sorted[left]=temp
    for i in range(left+1): #left was at index 2 so 2+1=3 covers 0,1,2 indices
        print(sorted[i],end=" ")
    print()
    return "Removed Duplicates Successfully"
print(check())