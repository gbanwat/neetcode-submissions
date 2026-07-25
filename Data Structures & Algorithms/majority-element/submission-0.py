from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_mark=len(nums)/2
        d=defaultdict(int)
        for num in nums:
            d[num]+=1
        for num in d:
            if d[num]>=majority_mark:
                return num
        