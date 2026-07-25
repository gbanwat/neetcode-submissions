class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        v_ind=0
        for num in nums:
            if num!=val:
                nums[v_ind]=num
                v_ind+=1
        return v_ind
        