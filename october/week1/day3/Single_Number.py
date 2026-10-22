#brute force method
#every number appears twice except on enumber find that number
nums=[4,2,1,2,1]
def check():
    count=0
    n=len(nums)
    for i in range(n):
        for j in range(n):
            if nums[i]==nums[j]:
                count+=1
        if count==1:
            return nums[i]
print(check())
#############################
def check2():
    result=0
    for i in range(len(nums)):
        result=result^nums[i]
    return result
print(check2())
#convert the number to binary then if 1^0 or 0^1 = 1 ...if 1^1 or 1 0^0 = 0