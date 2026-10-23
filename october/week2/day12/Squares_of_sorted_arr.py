num2=[-4,-1,0,3,10]
res=[0]*len(num2)
def check2():
    left=0
    right=len(num2)-1
    pos=len(num2)-1
    while left<=right:
        if abs(num2[left])>abs(num2[right]):
            res[pos]=num2[left]*num2[left]
            left+=1
        else:
            res[pos]=num2[right]*num2[right]
            right-=1
        pos-=1
    return res
print(check2())