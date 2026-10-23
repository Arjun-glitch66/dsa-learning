#move zeroes to the end but keep the order of non zero elements unchanged 
num=[0,1,0,3,12]
def check():
    left=0
    for right in range(len(num)):
        if num[right]!=0:
            num[left],num[right]=num[right],num[left]
            left+=1
    print(num[::]) #prints the whole array
    #or
    for i in range(len(num)):
        print(num[i],end=" ")
    print()

    return "Sucess"
print(check())