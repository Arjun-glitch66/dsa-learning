s="abba"
def check():
    count = 0
    for i in range(len(s)):
        #odd
        left=i
        right=i
        while left>=0 and right<len(s):
            if s[left]!=s[right]:
                break
            count+=1
            left-=1
            right+=1
        #even
        left=i
        right=i+1
        while left>=0 and right<len(s):
            if s[left]!=s[right]:
                break
            count+=1
            left-=1
            right+=1
    return count
result = check()
print(result)