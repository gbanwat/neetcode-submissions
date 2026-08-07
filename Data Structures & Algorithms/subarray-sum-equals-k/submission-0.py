class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counter=0
        total=0
        d={}

        for i in range(len(nums)):
            total+=nums[i]
            if total==k:
                counter+=1
            if total-k in d:
                counter+=d[total-k]
            if total not in d:
                d[total]=1
            else:
                d[total]+=1
        return counter
    
                    



            
            





        