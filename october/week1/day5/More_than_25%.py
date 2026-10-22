#A majority element of 25% is a number that appears more than n/4 times in an array of length n
#7/4 is 1.75
num=[1,2,1,1,1,2,3]
def check():
    dict={}
    for n in num:
        if n in dict:
            dict[n]+=1
        else:
            dict[n]=1
    for n in dict:
        if dict[n]>=len(num)/4:
            print(n) # gives 1 and 2 since their count is more than 1.75
    return dict #{1: 4, 2: 2, 3: 1}
print(check())
