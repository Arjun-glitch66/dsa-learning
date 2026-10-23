#Two strings are anagrams if they contain exactly the same characters with the same frequencies, but the order can be different.
s="anagram"
t="nagaram"
def check():
    d1={}
    d2={}
    for ch in s:
        if ch in d1:
            d1[ch]+=1
        else:
            d1[ch]=1
    print(d1)
    for ch in t:
        if ch in d2:
            d2[ch]+=1
        else:
            d2[ch]=1
    print(d2)
    if d1==d2:
        print("They have same characters with same frequencies but order can be differed")
        return True
    else:
        return False
print(check())