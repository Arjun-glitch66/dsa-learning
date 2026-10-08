s="a-bC-dEf-ghIj"
def reverse(s):
    s=list(s) #string to list
    left=0
    right=len(s)-1
    while left<right:
        if not s[left].isalpha():
            left+=1
            continue
        if not s[right].isalpha():
            right-=1
            continue
        s[left],s[right]=s[right],s[left]
        left=left+1
        right=right-1
    s="".join(s) #list to string 
    return s
result=reverse(s)
print(result)