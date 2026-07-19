class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s=dict.fromkeys(set(s),0)
        dict_t=dict.fromkeys(set(t),0)
        for i in s:
            dict_s[i]+=1
        #print(dict_s)
        for i in t:
            dict_t[i]+=1
        #print(dict_t)
        if dict_s==dict_t:
            return True
        else:
            return False
