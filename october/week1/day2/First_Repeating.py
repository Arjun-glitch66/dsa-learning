#To find the first value whihc gets repeated
nums=[1,2,3,2,3]
def check():
    count=0
    seen=set() 
    for n in nums:
        count+=1
        if n in seen:
            return n,count #count tells the index+1 th position
            break
        seen.add(n)
print(check())