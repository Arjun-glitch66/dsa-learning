val=[]
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
node1=Node(1)
node2=Node(2)
node3=Node(2)
node4=Node(1)
node1.next=node2
node2.next=node3
node3.next=node4
head=node1
current=head
while current is not None:
    val.append(current.val)
    current=current.next
def check():
    left=0
    right=len(val)-1
    while left<right:
        if val[left]!=val[right]:
            return False
        else:
            left=left+1
            right=right-1
    return True
result=check()
print(result)