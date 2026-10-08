s="abca" 
def check(s):
    left=0
    right=len(s)-1
    skip=0
    while left<right:
        if s[left]!=s[right]:
            if skip<1: # only one skip allowed
                skip_ind=left
                new=s[:skip_ind]+s[skip_ind+1:] #[starting:1]+[1+1:till end]
                left+=1
                skip+=1
                continue #goes to while cond
            return False
        else:
            left=left+1
            right=right-1
    print(new)
    return True
result=check(s)
print(result)