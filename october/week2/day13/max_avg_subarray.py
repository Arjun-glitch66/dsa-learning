def findMaxAverage(nums,k):
    current_sum=0

    for i in range(k):
        current_sum+=nums[i]

    max_sum=current_sum

    for i in range(k,len(nums)):
        current_sum+=nums[i]
        current_sum-=nums[i-k]

        if current_sum>max_sum:
            max_sum=current_sum

    return max_sum/k


nums=[1,12,-5,-6,50,3]
k=4
print(findMaxAverage(nums,k))