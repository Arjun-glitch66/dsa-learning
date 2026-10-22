#To find the duplicate number within the specified index limit k
nums=[1,2,2,4]
k=3
def check():
    last={} #dictionery
    for i in range(len(nums)):
        if nums[i] in last: #last checks whether the key is present in dictioonery or not 
            if i-last[nums[i]]<=k: #at i=2, 2-last[nums[2]], 2-last[2], 2-1=1 
                return True
        last[nums[i]]=i #last={1: 0,2: 1}
    return False
print(check())

