class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l=0
        i=0
        r=len(nums)-1

        while i<=r:
            if nums[i]==0:
                a=nums[l]
                nums[l]=nums[i]
                nums[i]=a
                i+=1
                l+=1
            elif nums[i]==2:
                a=nums[i]
                nums[i]=nums[r]
                nums[r]=a
                r-=1
            else:
                i+=1
        return nums
     









        """
        Do not return anything, modify nums in-place instead.
        """
        