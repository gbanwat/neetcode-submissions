class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) in [0,1]:
            return True
        def ispalindrome(s):
            l=0
            r=len(s)-1
            while l<r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            else: return True
        
        L=0 
        R=len(s)-1
        while L<R:
            if s[L]!=s[R]:
                if ispalindrome(s[L+1:R+1]):
                    return True
                elif ispalindrome(s[L:R]):
                    return True
                else:
                    return False
            L+=1
            R-=1
        return True
        