nums1=[1,2,2,1]
nums2=[2,2]

def intersection(num1,num2):
    seen=set(nums1) #{1,2}
    answer=[]
    for num in nums2:
        if num in seen:
            answer.append(num)
            seen.remove(num) #without this op = [2,2]

    return answer

result=intersection(nums1,nums2)
print(result)