s="ab"
goal="ba"
def check():
    if len(s)!=len(goal):
        return False
    first=-1
    second=-1
    for i in range(len(s)):
        if s[i]!=goal[i]:
            if first==-1:
                first=i
            else:
                second=i
    if second==-1:
        return False
    return s[first]==goal[second] and s[second]==goal[first]
print(check())