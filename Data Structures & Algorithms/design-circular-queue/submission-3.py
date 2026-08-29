class ListNode:
    def __init__(self,val,prev,nxt):
        self.val=val
        self.prev=prev
        self.nxt=nxt
        

class MyCircularQueue:

    def __init__(self, k: int):
        self.space=k
        self.left=ListNode(0,None,None)
        self.right=ListNode(0,self.left,None)
        self.left.nxt=self.right

        

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        cur=ListNode(value,self.right.prev,self.right)

        self.right.prev.nxt=cur
        self.right.prev=cur
        self.space-=1
        return True

        

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        self.left.nxt=self.left.nxt.nxt
        self.left.nxt.prev=self.left
        self.space+=1
        return True


        

    def Front(self) -> int:
        if self.isEmpty(): 
            return -1
        else:
            return self.left.nxt.val

        

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.right.prev.val

        

    def isEmpty(self) -> bool:
        if self.left.nxt==self.right:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.space==0:
            return True
        else:
            return False

        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()