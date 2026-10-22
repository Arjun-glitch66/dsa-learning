nums=[1,2,2,4]
def check():
    seen=set() #set stores only unique elements
    for n in nums:
        if n in seen:
            return True
        seen.add(n)
    return False
print(check())