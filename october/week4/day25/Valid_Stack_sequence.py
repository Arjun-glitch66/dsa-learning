pushed=[1,2,3,4,5]
popped=[4,5,3,2,1]
def check():
    stack=[]
    j=0
    for i in range(len(pushed)):
        stack.append(pushed[i])
        while len(stack)>0 and stack[-1]==popped[j]:
            stack.pop()
            j+=1
    return len(stack)==0
print(check())