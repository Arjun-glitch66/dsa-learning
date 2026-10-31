s="abcde"
goal="cdeab"
def check():
    if len(s)!=len(goal):
        return False
    temp=s+s
    if goal in temp:
        return True
    return False
print(check())