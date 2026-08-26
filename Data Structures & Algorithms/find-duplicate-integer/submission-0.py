class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d=dict.fromkeys(nums,0)
        for i in range(len(nums)):
            d[nums[i]]+=1
            if d[nums[i]]>1:
                return nums[i]

        