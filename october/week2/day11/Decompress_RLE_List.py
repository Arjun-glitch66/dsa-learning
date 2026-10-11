
def decompress(nums):
    total=0
    for i in range(0,len(nums),2):
        total+=nums[i]
    result=[0]*total
    k=0
    for i in range(0,len(nums),2):
        freq=nums[i]
        val=nums[i+1]
        for j in range(freq):
            result[k]=val
            k+=1
    return result
nums=[1,2,3,4]
print(decompress(nums))
