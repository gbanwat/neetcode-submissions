class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=""
        for i in s:
            if i.isalnum():
                a+=i
        a=a.lower()
        i=0
        j=len(a)-1
        #return a
        while i<j:
            if a[i]!=a[j]:
                return False
            i+=1
            j-=1
            
        return True


        