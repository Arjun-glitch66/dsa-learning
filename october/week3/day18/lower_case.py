s="Hello"
def check():
    result=""
    for ch in s:
        if ch>='A' and ch<='Z':
            result=result+chr(ord(ch)+32)
        else:
            result=result+ch
    return result
print(check())