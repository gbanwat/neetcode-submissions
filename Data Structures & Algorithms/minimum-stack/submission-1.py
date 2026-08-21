class MinStack:

    def __init__(self):
        self.lst=[]
        self.mini=[]
        

    def push(self, val: int) -> None:
        self.lst.append(val)
        val=min(val, self.mini[-1] if self.mini else val)
        self.mini.append(val)

    def pop(self) -> None:
        self.lst.pop()
        self.mini.pop()
        

    def top(self) -> int:
        return self.lst[-1]
        

    def getMin(self) -> int:
        return self.mini[-1]
        
