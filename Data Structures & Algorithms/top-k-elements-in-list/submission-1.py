class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #d={}
        #for i in nums:
        #    if i not in d:
        #        d[i]=1
        #    else:
        #        d[i]+=1
        #return sorted(d,key=d.get,reverse=True)[:k]
        count={}
        freq=[[] for i in range(len(nums)+1)]

        for i in nums:
            count[i]=1+count.get(i,0)
        
        for key,v in count.items():
            freq[v].append(key)
        res=[]
        for i in range(len(nums),0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res
        