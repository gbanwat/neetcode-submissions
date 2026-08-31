class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
       d=dict.fromkeys(set(nums),0)
       target=len(nums)/3
       for n in nums:
        d[n]+=1
       res=[]
       for i in d:
        if d[i]>target:
            res.append(i)
       return res
        
        