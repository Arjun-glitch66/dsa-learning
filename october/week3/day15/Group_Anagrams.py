words=["eat","tea","tan","ate","nat","bat"]
def check():
    list=[]
    for w in words:
        dict={}
        for ch in w:
            if ch in dict:
                dict[ch]+=1
            else:
                dict[ch]=1
        print (w,dict)
        list=list+[[w,dict]] #if list is appended here after each iteration the dictionery gets appeneded
    #list=list+[[w,dict]]...if this is done like this it takes only the last dictionery i.e bat,b:1,a:1,t:1 (refer  perumation of strings for ssimilar type) 
    print("Dictionery converted to list")
    print(list)
    groups=[]
    group_freq=[]
    for i in range(len(list)):
        found=False
        for j in range(len(group_freq)): #first iteration its empty so j loop doesnt run becauase len(group_freq)=0
            if group_freq[j]==list[i][1]:
                groups[j]=groups[j]+[list[i][0]]
                found=True
                break
        if found==False: #for first iteration its empty so create 
            groups=groups+[[list[i][0]]] #groups=groups+[['eat']] creates first subgroup ...from second iteration onwards if found=False it creates another subgroup else it keeps on adding in the same subgroup
            group_freq=group_freq+[list[i][1]] #{'e': 1, 'a': 1, 't': 1},.....and so on
    return groups

print(check())