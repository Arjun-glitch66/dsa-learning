def findMaxAverage(nums,k):
    current_sum=0

    for i in range(k):
        current_sum+=nums[i]

    max_sum=current_sum