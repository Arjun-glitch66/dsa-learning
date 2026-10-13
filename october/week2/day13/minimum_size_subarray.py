num=[2,3,1,2,4,3]
target=7
def find():
    total=0
    left=0
    minimum=len(num)+1 #set to highest value 
    for right in range(len(num)): #right expands
        total+=num[right]
        while total>=target: # 8>=7
            length=right-left+1 # right is index 3 left is index 0 so 3-0+1=4 is the length of substring
            total-=num[left] #left shrinks
            left+=1
            if length<minimum:
                minimum=length

    if (minimum==len(num)+1):
        return 0
    return minimum
res=find()
print(res)