s="()[]{}"
def check():
    stack=[]
    for ch in s:
        if ch=="(" or ch=="[" or ch=="{":
            stack=stack+[ch]
        else:
            if len(stack)==0:
                return False
            top=stack[-1]
            if (ch==")" and top!="(") or (ch=="]" and top!="[") or (ch=="}" and top!="{"):
                return False
            stack=stack[:-1]
    return len(stack)==0
print(check())