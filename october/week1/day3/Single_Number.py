#brute force method
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
