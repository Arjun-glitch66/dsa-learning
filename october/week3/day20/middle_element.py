nums=[2,3,-1,8,4]
def check():
    total=0
    for n in nums:
        total=total+n
    left=0
    for i in range(len(nums)):
        right=total-left-nums[i]
        if left==right:
            return i
        left=left+nums[i]
    return -1
print(check())

