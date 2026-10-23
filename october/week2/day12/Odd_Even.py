num=[4,2,5,7]
def check():
    left=0
    right=1
    while left<len(num) and right<len(num):
        if num[left]%2==0: #if elif else block is treated as one block .... if if else here the two ifs are checked becauuse they are not treated as one block
            left+=2
        elif num[right]%2!=0:
            right+=2
        else:
            num[left],num[right]=num[right],num[left]
            left+=2
            right+=2
    return num

print(check())
            
