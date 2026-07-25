class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d_list=[]
        for s in strs:
            d1=dict.fromkeys(s,0)
            for a in s:
                d1[a]+=1
            d_list.append((s,d1))
        
        result=[]
        while d_list:
            s_current,d_current=d_list.pop(0)
            group=[s_current]
            remaining_dict_list=[]
            for d in d_list:
                if d_current==d[1]:
                    group.append(d[0])
                else:
                    remaining_dict_list.append(d)
            d_list=remaining_dict_list
            result.append(group)
        return result

        





