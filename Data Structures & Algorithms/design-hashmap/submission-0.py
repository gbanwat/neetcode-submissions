class LLNode:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None


class MyHashMap:
    def hash(self,key):
        return key%10**4
        
    def __init__(self):
        self.map=[LLNode(0,0) for _ in range(10**4)]
        
    def put(self, key: int, value: int) -> None:
        index=self.hash(key)
        current=self.map[index]

        while current.next:
            if current.next.key==key:
                current.next.value=value
                return
            current=current.next
        current.next=LLNode(key,value)

        

    def get(self, key: int) -> int:
        index=self.hash(key)
        current=self.map[index]

        while current.next:
            if current.next.key==key:
                return current.next.value
            current=current.next
        else:
            return -1

        

    def remove(self, key: int) -> None:
        index=self.hash(key)
        current=self.map[index]

        while current.next:
            if current.next.key==key:
                current.next=current.next.next
                return
            current=current.next

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)