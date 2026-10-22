nums=[4,3,2,7,8,2,3,1]
def check():
    dict={}
    for n in nums:
        if n in dict:
            dict[n]+=1
        else:
            dict[n]=1
    for n in dict:
        if dict[n]==2:
            print(n)
    return dict
print(check())
#######################
#in place marking approach
def check2():
    result=[]
    for i in range(len(nums)):
        n=abs(nums[i])
        index=n-1
        if nums[index]<0:
            result=result+[n] #If the value is already negative, that number has been seen before, so add it to result
        else:
            nums[index]=-nums[index]
    for i in range(len(nums)):
        print(nums[i])
    return result #2,3 are the numbers which gets repeated and also they are the ones which get checked as less than zero
print(check2())
        