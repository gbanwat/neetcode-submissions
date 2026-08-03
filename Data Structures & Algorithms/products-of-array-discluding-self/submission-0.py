class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre=[0 for _ in range(len(nums))]
        suf=[0 for _ in range(len(nums))]
        product=[]
        for i in range(len(nums)):
            if i==0:
                pre[i]=1
                suf[-1]=1
            else:
                pre[i]=pre[i-1]*nums[i-1]
                suf[-1-i]=suf[-i]*nums[-i]
       
        #print(suf)
        for i in range(len(nums)):
            product.append(pre[i]*suf[i])
        return product
            
