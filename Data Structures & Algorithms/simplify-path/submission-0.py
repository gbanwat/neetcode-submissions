class Solution:
    def simplifyPath(self, path: str) -> str:
        a=path.split('/')
        
        stack=[]
        for e in a:
            if e=="." or e=="":
                continue
            elif e==".." and len(stack)!=0:
                stack.pop()
            elif e==".." and len(stack)==0:
                continue
            else:
                l="/"+e
                stack.append(l)
        if len(stack)==0:
            stack.append("/")
        res=""
        for i in stack:
            res="".join([res,i])
        return res
