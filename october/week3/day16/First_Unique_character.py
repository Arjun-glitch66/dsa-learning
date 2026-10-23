s="leetcode"
def check():
    d1={}
    for ch in s:
        if ch in d1:
            d1[ch]+=1
        else:
            d1[ch]=1

    for i in range(len(s)):
        if d1[s[i]]==1:
            return i
    return -1
print(check())