#index difference is atmost k
# value difference is atmost t
num=[1,5,9,1]
k=2
t=3
def check():
    dict={}
    for i in range(len(num)): #for n in num ..this approach is also used in some of the previous sums do check
        if num[i] in dict:
            if i-dict[num[i]]<=k and num[i]-num[dict[num[i]]]<=t: #here the value difference is num[3]-num[dict[num[3]]]...1-num[dict[1]]..1-num[0]...1-1=0 satisfies but 3- dict[1]...3-0=3 doest not satisfies so False
                dict[num[i]]+=i #unwanted 
                print(dict) #but still if the prev statement runs becuase the if condition itself is false but still {1: 3, 5: 1, 9: 2}
                return True

        else:
            dict[num[i]]=i #{1: 0, 5: 1, 9: 2} till the 0th,1st,2nd index 
    return False
print(check())