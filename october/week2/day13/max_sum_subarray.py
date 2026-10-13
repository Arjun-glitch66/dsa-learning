num=[2,3,4,5,5]
k=2
def find():
    total=0
    for i in range(k):
        total+=num[i]

    maxx=total
    for i in range(k,len(num)):
        total+=num[i]
        total-=num[i-k]
        if total>maxx:
            maxx=total

    return maxx
result=find()
print(result)