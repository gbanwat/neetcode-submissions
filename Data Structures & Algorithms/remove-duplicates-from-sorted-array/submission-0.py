class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        #l=len(nums)
        while i+1<len(nums):
            if nums[i+1]==nums[i]:
                nums.pop(i)
            else:
                i+=1
        return len(nums)
        