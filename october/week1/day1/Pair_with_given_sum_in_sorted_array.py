arr=[1,2,3,4,5,6]
target=7

def countPairs(arr,target):
    left=0
    right=len(arr)-1
    count=0

    while left<right:
        total=arr[left]+arr[right]

        if total==target:
            count+=1
            left+=1
            right-=1
        elif total<target:
            left+=1
        else:
            right-=1

    return count

print(countPairs(arr,target))