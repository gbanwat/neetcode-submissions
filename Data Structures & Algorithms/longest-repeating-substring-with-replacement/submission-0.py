class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        r=0
        d=dict.fromkeys(s,0)
        max_len=0

        for r in range(len(s)):
            d[s[r]]+=1
            if len(s[l:r+1])-max(d.values())>k:
                #l+=1
                d[s[l]]-=1
                l+=1
            else:
                max_len=max(len(s[l:r+1]),max_len)
        return max_len
            


        