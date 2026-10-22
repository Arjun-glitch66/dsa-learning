#to find the prefix sum of speicified range
nums=[1,2,3,4,5]
l=1 #position not index
r=3 
result=[0]*(r-l+1) # 3-1+1=3 ...result=[0,0,0]
result[0]=nums[l-1]
def check():
    for i in range(l-1,r):
        result[i]=result[i-1] + nums[i]
        ans=result[-1]
    return result,ans
print(check())
