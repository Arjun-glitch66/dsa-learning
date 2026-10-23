#removing duplicates froms sorted array but a number can appear twice
num=[1,1,1,2,2,3]
def check():
    left=2
    for right in range(2,len(num)):
        if num[right]!=num[left-2]:
            num[left]=num[right]
            left+=1
    print(num[:left])
print(check())
