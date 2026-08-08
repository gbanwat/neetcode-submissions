class Solution:
    def isPalindrome(self, s: str) -> bool:
            a=""
            for i in s:
                if i.isalnum():
                    a+=i
            a=a.lower()
            i=0
            j=len(a)-1

            while i<j:
                if a[i]!=a[j]:
                    return False
                i+=1
                j-=1
            
            return True

    def validPalindrome(self, s: str) -> bool:
        counter=0
        a=""
        for i in s:
            if i.isalnum():
                a+=i
        a=a.lower()
        i=0
        j=len(s)-1

        while i<j:
            if a[i]!=a[j] and counter==0:
                counter+=1
                if a[i+1]==a[j] and a[i]!=a[j-1]:
                    i+=1
                elif a[i]==a[j-1] and a[i+1]!=a[j]:
                    j-=1
                elif a[i+1]==a[j] and a[i]==a[j-1]:
                    if self.isPalindrome(a[i+1:j+1]):
                        i+=1
                    elif self.isPalindrome(a[i:j]):
                        j-=1

                elif a[i+1]!=a[j] and a[i]!=a[j-1]:
                    return False




            elif a[i]!=a[j] and counter!=0:
                return False
            
            else:
                i+=1
                j-=1
        
        return True



        