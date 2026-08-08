class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l=min(len(word1),len(word2))
        a=""
        i=0
        while i<l:
            a+=word1[i]+word2[i]
            i+=1
        if i==len(word1):
            a+=word2[i:]
        elif i==len(word2):
            a+=word1[i:]
        return a

        