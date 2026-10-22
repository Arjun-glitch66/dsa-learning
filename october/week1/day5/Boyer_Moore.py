#to find majority
num=[2,1,1,1,2,2,2]
def check():
    votes=0
    candidates=0
    for i in range(len(num)):
        if votes==0:
            candidates=num[i]
        if num[i]==candidates:
            votes+=1
        else:
            votes-=1
    return candidates
print(check())
#if else block is treated as one block so it executes in a single run
#initially votes=0 so candidate is 2
#2=2 vote=1
#1!=2 vote=0
#vote=0 therefore candidate=1 (2nd index)
#1=1 votes=1
#2!=1 votes=0
#votes=0 therefore candidate=2(5th index)
#2=2 vote=1
#2=2 vote=2 
#candidate=2
