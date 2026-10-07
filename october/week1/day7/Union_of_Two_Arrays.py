nums1=[1,2,2,4]
nums2=[2,3,4]

def union(nums1,nums2):
    answer=nums1.copy()
    for num in nums2:
        answer.append(num)
    return answer

result=union(nums1,nums2)
print(result)