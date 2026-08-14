class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_arr=[]
        #p=0
        ln=0
        max_ln=0

        for p in s:
            if p in sub_arr:
                idx=sub_arr.index(p)
                del sub_arr[:idx+1]
                sub_arr.append(p)
                ln=len(sub_arr)
                max_ln=max(ln,max_ln)
            else:
                sub_arr.append(p)
                ln=len(sub_arr)
                max_ln=max(ln,max_ln)
        return max_ln
        