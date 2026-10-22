#build array from the index of current element
num=[0, 2, 1, 5, 3, 4]
ans=[0]*len(num)
def build():
    for i in range(len(num)):
        ans[i]=num[num[i]] #[0, 1, 2, 4, 5, 3]
    return ans
print(build())
