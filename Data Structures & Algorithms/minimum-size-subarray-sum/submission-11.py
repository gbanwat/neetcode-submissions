class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        r=0
        ln=0
        min_ln=len(nums)
        s=0

        if sum(nums)<target:
            return 0
        
        for r in range(len(nums)):
            s+=nums[r]
            ln=len(nums[l:r+1])
            while s>=target:
                min_ln=min(min_ln,r+1-l)
                s-=nums[l]
                l+=1
        return min_ln


        