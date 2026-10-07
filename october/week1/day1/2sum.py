# Two Sum

nums = [3, 2, 4]
target = 6

def twosum(nums, target):
    seen = {}

    for i in range(len(nums)):
        complement = target - nums[i]

        if complement in seen:
            print(f"{complement}+{nums[i]}={target}") #prints the the key alone of the complent= 2 + 4 =6
            print("The indices in the nums list are; ")
            return [seen[complement], i] # complement is the key so seen[complement] gives the value of that which is 1#[seen[2],2] = [1,2] are the indices which is the output

        else:
            seen[nums[i]] = i #seen[nums[0]]=0 gives seen[3]=0 means key is 3 and value is 0 key-value pair dictionery

answer = twosum(nums, target)
#without parameters also possible but with parameters means the user can put any list and target in the future while calling the method 

print(answer)