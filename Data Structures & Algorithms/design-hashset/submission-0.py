class LLNode:
    def __init__(self,data):
        self.data=data
        self.next=None


class MyHashSet:

    def __init__(self):
        self.set=[LLNode(0) for _ in range(10**4)]

    def hash(self,data):
        return data % 10**4

    def add(self, key: int) -> None:
        index=self.hash(key)
        current=self.set[index]

        while current.next:
            if current.next.data==key:
                return
            current=current.next

        current.next=LLNode(key)
        

    def remove(self, key: int) -> None:
        index=self.hash(key)
        current=self.set[index]

        while current.next:
            if current.next.data==key:
                current.next=current.next.next
                return
            current=current.next

    
    def contains(self, key: int) -> bool:
        index=self.hash(key)
        current=self.set[index]

        while current.next:
            if current.next.data==key:
                return True
            current=current.next
        return False

        
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)