word="abcdefd"
ch="d"
def reversePrefix(word,ch):
    word=list(word)
    right=-1
    for i in range(len(word)):
        if word[i]==ch:
            right=i
            break
    if right!=-1:
        left=0
        while left<right:
            word[left],word[right]=word[right],word[left]
            left+=1
            right-=1
    return "".join(word)
print(reversePrefix(word,ch))