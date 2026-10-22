num=[4, 3, 2, 7, 8, 2, 3, 1]
def check():
    for i in range(len(num)):
        n=abs(num[i]) #abs means positive ...n=abs(num[0])..n=4
        index=n-1 #4-1 =3
        if num[index]>0: #num[3]=7
            num[index]=-num[index] #-7
#[-4, -3, -2, -7, 8, 2, -3, -1] ...during iteration if its already negative no need to change anything 
    result=[]
    for i in range(len(num)):
        if num[i]>0:
            result=result+[i+1] # only the index 4 and 5 are positive therefore 4+1 and 5+1 to represent their positions
    return result
print(check())