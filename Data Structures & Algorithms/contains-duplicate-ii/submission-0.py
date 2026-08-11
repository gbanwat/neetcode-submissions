class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
     l=0
     r=1
     while l<len(nums):
        if nums[l] in nums[l+1:min(l+k+1,len(nums))]:
            return True
        else:
            l+=1
            #r+=1
     return False