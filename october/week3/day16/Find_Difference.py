#dict to list convertion not necessary
s="abcd"
t="abcde"
def check():
    d1={}
    l1=[]
    for ch in s:
        if ch in d1:
            d1[ch]+=1
        else:
            d1[ch]=1
    l1=l1+[d1] #convert dictionery to list (refer group anagarams) there it was inside for loop becuase it needs to be appended after every iteration...but here its just a single word so convertion is outside the for loop
    print(d1)
    print(l1)

    d2={}
    l2=[]
    for ch in t:
        if ch in d2:
            d2[ch]+=1
        else:
            d2[ch]=1
    l2=l2+[d2]
    print(d2)
    print(l2)

    for ch in t:
        if ch not in d1:
            return ch
print(check())
