#permutation measn order doesnt matter 
s1="ab"
s2="eidbaooo" #this has ba so true becuase order doesnt matter 
def check():
    target={'a':1,'b':1}
    #creation of window
    #dicty={}
    for i in range(len(s2)-len(s1)+1): #iteerates 7 times +1 in order to include the last window also 
        window=s2[i:i+len(s1)]
        dicty={}
        for ch in window:
            if ch in dicty:
                dicty[ch]+=1
            else:
                dicty[ch]=1
        print(window,dicty)
        if dicty==target:
            print("True")
    return "Over"
print(check())  
#window,dicty output if dicty is placed beofre outer for loop 
#ei {'e': 1, 'i': 1}
#id {'e': 1, 'i': 2, 'd': 1}
#db {'e': 1, 'i': 2, 'd': 2, 'b': 1}
#ba {'e': 1, 'i': 2, 'd': 2, 'b': 2, 'a': 1}
#ao {'e': 1, 'i': 2, 'd': 2, 'b': 2, 'a': 2, 'o': 1}
#oo {'e': 1, 'i': 2, 'd': 2, 'b': 2, 'a': 2, 'o': 3}
#oo {'e': 1, 'i': 2, 'd': 2, 'b': 2, 'a': 2, 'o': 5}

#if before inner for loop
#ei {'e': 1, 'i': 1}
#id {'i': 1, 'd': 1}
#db {'d': 1, 'b': 1}
#ba {'b': 1, 'a': 1}
#True
#ao {'a': 1, 'o': 1}
#oo {'o': 2}
#oo {'o': 2}
#Over