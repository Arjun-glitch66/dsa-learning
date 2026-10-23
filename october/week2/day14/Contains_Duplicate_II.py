num=[1,2,3,1]
k=3
def chehck():
    dict={} 
    for i in range(len(num)):
            if num[i] in dict:
                if i-dict[num[i]]<=k: #3-dict[num[3]]...3-dict[1]...3-0=3<=k
                    dict[num[i]]+=i #unwanted statement 
                    print(dict) #but still if it runs {1: 3, 2: 1, 3: 2} 
                    return True   
            else:
                dict[num[i]]=i #{1: 0, 2: 1, 3: 2} till the 0th,1st,2nd index 
    return False
print(chehck())    