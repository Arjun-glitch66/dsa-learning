num=[1,2,3,4,5,6]
k=3

def find():
    tot=0 # this can be written as global varibale only when it comes under one class 
    #first window
    for i in range(k):
        tot+=num[i]

    maxx=tot
    #after first window 
    for i in range(k,len(num)): #(3,6)
        tot+=num[i] #incoming index 3 
        tot-=num[i-k] #outgoing [3-3] = 0th index
        if tot>maxx:
            maxx=tot
    avg=maxx/k
    return avg
res=find()
print(res)
