class Solution:
    def isValid(self, s: str) -> bool:
        open_=['[','(','{']
        close_=[']',')','}']
        res=[]

        for i in range(len(s)):    
            if s[i] in open_:
                res.append(s[i])
            elif s[i] in close_ and len(res)!=0:
                a=res.pop()
                if open_.index(a)!=close_.index(s[i]):
                    return False
            elif s[i] in close_ and len(res)==0:
                return False
            
        if len(res)!=0:
            return False
        else:
            return True
            
            

                
                
                

        