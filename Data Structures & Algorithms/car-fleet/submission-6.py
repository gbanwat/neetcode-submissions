class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ps=[]
        for p in range(len(position)):
            ps.append([position[p],speed[p]])
        ps.sort(reverse=True)

        time=[]
        for p,s in ps:
            time.append((target-p)/s)
        stack=[]
        fleet=len(position)
        for t in range(len(time)):
            if len(stack)==0 or stack[-1]<time[t]:
                stack.append(time[t])
        return len(stack)
        
        