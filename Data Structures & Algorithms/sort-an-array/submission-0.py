class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(nums):
            if len(nums)<=1:
                return nums
            mid=len(nums)//2
            left_arr=nums[:mid]
            right_arr=nums[mid:]

            left_arr=merge_sort(left_arr)
            right_arr=merge_sort(right_arr)

            return merge(left_arr,right_arr)

        def merge(left_arr,right_arr):
            i,j=0,0
            new_arr=[]
            while i<len(left_arr) and j<len(right_arr):
                if left_arr[i]<right_arr[j]:
                    new_arr.append(left_arr[i])
                    i+=1
                else:
                    new_arr.append(right_arr[j])
                    j+=1
            new_arr.extend(left_arr[i:])
            new_arr.extend(right_arr[j:])

            return new_arr
        return merge_sort(nums)



        