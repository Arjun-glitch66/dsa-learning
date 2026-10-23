#2 pointer approach for removing duplicates
#sorted array
nums=[1,2,1,1,3,2]
num2=sorted(nums)
print(num2) #[1,1,1,2,2,3]
def check():
    left=0
    for right in range(1,len(num2)):
        if num2[left]==num2[right]:
            continue
        else:
            left+=1
            temp=num2[right]
            num2[right]=num2[left]
            num2[left]=temp
    for i in range(left+1): #left was at index 2 so 2+1=3 covers 0,1,2 indices
        print(num2[i],end=" ") #if here return num2[i] is used means it gives only 1 as output because return once it runs it stops the whole program
    print()
    return "Removed Duplicates Successfully"
print(check())