words=["bella","label","roller"]
def commonChars(words):
    count={}
    for ch in words[0]:
        if ch in count:
            count[ch]=count[ch]+1
        else:
            count[ch]=1
    for word in words[1:]:
        current={}
        for ch in word:
            if ch in current:
                current[ch]=current[ch]+1
            else:
                current[ch]=1
        for ch in count:
            if ch in current:
                if current[ch]<count[ch]:
                    count[ch]=current[ch]
            else:
                count[ch]=0
    answer=[]
    for ch in count:
        for i in range(count[ch]):
            answer.append(ch)
    return answer


result=commonChars(words)

print(result)