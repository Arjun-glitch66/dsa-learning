a=[1,5,10,20,40,80]
b=[6,7,20,80,100]
c=[3,4,15,20,30,70,80,120]

def intersection(a,b,c):
    i=0
    j=0
    k=0
    answer=[]
    while i<len(a) and j<len(b) and k<len(c):
        if a[i]==b[j]==c[k]:
            answer.append(a[i])
            i+=1
            j+=1
            k+=1
        elif a[i]<b[j]:
            i+=1

        elif b[j]<c[k]:
            j+=1

        else:
            k+=1
    return answer
result=intersection(a,b,c)
print(result)