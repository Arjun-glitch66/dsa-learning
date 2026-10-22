num=[2,0,3]
def check():
    for x in range(len(num)):
        found=False
        for i in range(len(num)):
            if x==num[i]:
                found=True
                break
        if found==False:
            return x
print(check())
