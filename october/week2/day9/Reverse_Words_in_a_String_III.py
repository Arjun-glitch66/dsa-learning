s="Let's take LeetCode contest"
def reverseWords(s):
    words=s.split()
    answer=[]
    for word in words:
        word=list(word)
        left=0
        right=len(word)-1
        while left<right:
            word[left],word[right]=word[right],word[left]
            left+=1
            right-=1
        answer.append("".join(word))
    return " ".join(answer)
print(reverseWords(s))