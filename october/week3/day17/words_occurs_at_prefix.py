sentence="i love eating burger"
searchWord="eat"
def check():
    words=sentence.split()
    for i in range(len(words)):
        if words[i][:len(searchWord)]==searchWord:
            return i+1
    return -1
print(check())