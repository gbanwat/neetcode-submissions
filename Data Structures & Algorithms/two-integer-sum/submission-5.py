class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_nums={}
        for i in range(len(nums)):
            dict_nums[nums[i]]=i
        print (dict_nums)
        for i in range(len(nums)):
            num_2=target-nums[i]
            if num_2 in dict_nums and i!=dict_nums[num_2]:
                return [i,dict_nums[num_2]]


    
        