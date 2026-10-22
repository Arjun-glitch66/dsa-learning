nums=[4,3,2,7,8,2,3,1]
def check():
    dict={}
    for n in nums:
        if n in dict:
            dict[n]+=1
        else:
            dict[n]=1
    for n in dict:
        if dict[n]==2:
            print(n)
    return dict
print(check())