# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a,b=l1,l2
        c=0
        d=[]
        e=None
        while ((a is not None ) or (b is not None )):
            i=a.val if a is not None else 0
            j=b.val if b is not None else 0
            if i+j+c < 10: 
                d.append(i+j+c)
                c=0
            else:
                d.append((i+j+c)%10)
                c=(i+j+c)//10
            a=a.next if a is not None else None
            b=b.next if b is not None else None
        if c :
            d.append(c)
                
        for i,a in enumerate(list(reversed(d))):
            if not i :
                e=ListNode(val=a)
            else:
                e=ListNode(val=a,next=e)

        return e


if __name__ =='__main__':
    a,b=[2,4,3],[5,6,4]
    def setnode(lit):
        for i ,a in enumerate(reversed(lit)):
            if not i :
                ist=ListNode(val=a)
            else:
                ist=ListNode(val=a,next=ist)
        return ist
    l1,l2=setnode(a),setnode(b)

    expected=[7,0,8]
    c=Solution()
    e=c.addTwoNumbers(l1,l2)
    d=[]
    while e is not None:
        d.append(e.val)
        e=e.next
        
    print(f'input : {a}, {b}')
    print(f'result: {d}, expected : {expected}')


