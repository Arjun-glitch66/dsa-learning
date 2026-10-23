#even at first and odd at end 
num=[3,1,2,4]
def check():
    left=0
    right=len(num)-1
    while left<right:
        if num[left]%2==0:
            left+=1
        elif num[right]%2!=0:
            right-=1
        else:
            num[left],num[right]=num[right],num[left]
            left+=1
            right-=1
    return num
print(check())