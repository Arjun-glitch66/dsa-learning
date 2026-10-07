nums1=[1,2,2,1]
nums2=[2,2]

def intersection(num1,num2):
    count={}
    answer=[]
    for num in nums1:
        if num in count:
            count[num]+=1
        else:
            count[num]=1

    for num in nums2:
        if num in count and count[num]>0:
            answer.append(num)
            count[num]-=1

    return answer

result=intersection(nums1,nums2)
print(result)