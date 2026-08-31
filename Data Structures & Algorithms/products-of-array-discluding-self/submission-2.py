class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suf=[0]*len(nums)
        pre=[0]*len(nums)
        res=[0]*len(nums)
        for i in range(len(nums)):
            if i==0:
                pre[i]=1
                suf[-1]=1
            else:
                pre[i]=pre[i-1]*nums[i-1]
                suf[-1-i]=suf[-i]*nums[-i]
        for i in range(len(nums)):
            res[i]=pre[i]*suf[i]
        return res
        