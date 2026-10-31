s="())"
def check():
    open=0
    add=0
    for ch in s:
        if ch=="(":
            open+=1
        elif open>0:
            open-=1
        else:
            add+=1
    return open+add
print(check())