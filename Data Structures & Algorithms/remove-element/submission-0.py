class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count=0
        for i in range(len(nums)):
            if nums[i]==val:
                nums[i]="_"
                count=count+1
        k=len(nums)-count
        while count!=0:
            for i in range(len(nums)):
                if nums[i]=="_":
                    nums.append(nums[i])
                    nums.pop(i)
                    count-=1
                    break
        return k
        