#A majority element is a number that appears more than n/2 times in an array of length n
#7/2 =3.5 so it shd appear 4 times here 2 appears 4 times 
num=[2,2,1,1,1,2,2]
def check():
    dict={}
    for n in num:
        if n in dict:
            dict[n]+=1
        else:
            dict[n]=1
        if dict[n]>=len(num)/2:
            return n,dict[n] #2,4 ...4 is the count 
print(check())
