from itertools import permutations
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1=dict.fromkeys(s1,0)
        for s in s1:
            d1[s]+=1
        l=0
        #r=len(s1)
        for r in range(len(s1),len(s2)+1):
            d2=dict.fromkeys(s2[l:r],0)
            for j in s2[l:r]:
                d2[j]+=1
            
            if d1==d2:
                return True
            
            l+=1
        return False
        

        