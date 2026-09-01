class LLNode:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.next=None

class MyHashMap:

    def __init__(self):
        self.hmap=[LLNode(0,0) for _ in range(10**4)]
        

    def put(self, key: int, value: int) -> None:
        idx=key%len(self.hmap)
        cur=self.hmap[idx]
        while cur.next!=None:
            if cur.next.key==key:
                cur.next.val=value
                return
            else:
                cur=cur.next
        cur.next=LLNode(key,value)
        

    def get(self, key: int) -> int:
        idx=key%len(self.hmap)
        cur=self.hmap[idx]
        while cur.next!=None:
            if cur.next.key==key:
                return cur.next.val
            cur=cur.next
        else:    
            return -1
        

    def remove(self, key: int) -> None:
        idx=key%len(self.hmap)
        cur=self.hmap[idx]
        while cur.next!=None:
            if cur.next.key==key:
                cur.next=cur.next.next
                return
            else:
                cur=cur.next
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)