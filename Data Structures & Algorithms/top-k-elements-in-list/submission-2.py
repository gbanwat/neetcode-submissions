class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #d={}
        #for i in nums:
        #    if i not in d:
        #        d[i]=1
        #    else:
        #        d[i]+=1
        #return sorted(d,key=d.get,reverse=True)[:k]
        count=dict.fromkeys(set(nums),0)
        for n in nums:
            count[n]+=1
        a= sorted(count,key=count.get,reverse=True)
        return a[:k]
        