nums=[1,2,3,4]
def check():
    result=[]
    total=0
    for i in range(len(nums)):
        total=total+nums[i]
        result=result+[total]
    return result
print(check())