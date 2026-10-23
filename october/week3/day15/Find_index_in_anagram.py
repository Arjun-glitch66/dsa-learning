#Given two strings, s and p, return all the starting indices of substrings in s that are anagrams of p.
s="cbaebabacd"
p="abc"
def check():
    d1={}
    for ch in p:
        if ch in d1:
            d1[ch]+=1
        else:
            d1[ch]=1
    print(d1)
    #create window (refer permutation of string)
    for i in range(len(s)-len(p)+1):
        window=s[i:i+len(p)]
        d2={}
        for ch in window:
            if ch in d2:
                d2[ch]+=1
            else:
                d2[ch]=1
        print(window,d2)
        if d2==d1:
            print("The starting index of the subsring anagram",window ,"is:", i)
    return "Over"
print(check())