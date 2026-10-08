s="A Man, a plan, a canal: Panama" 
def check(s):
    left=0
    right=len(s)-1
    while left<right:
        # cleanup is used to skip the :,and spaces
        if not s[left].isalnum():
            left+=1
            continue
        if not s[right].isalnum():
            right-=1
            continue
        if s[left].lower()!=s[right].lower(): #lower() to represent as amanaplanacanalpanama if not used A!=a conflicts
            return False
        else:
            left=left+1
            right=right-1

    return True
result=check(s)
print(result)