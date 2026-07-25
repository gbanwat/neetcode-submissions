class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d_list=[]
        for s in strs:
            d1=dict.fromkeys(s,0)
            for a in s:
                d1[a]+=1
            d_list.append((s,d1))
        res=[]
        while d_list:
            s_current,d_current=d_list.pop(0)
            remaining=[]
            group=[s_current]
            for d in d_list:
                if d[1]==d_current:
                    group.append(d[0])
                else:
                    remaining.append(d)
            d_list=remaining
            res.append(group)
        return res

        





