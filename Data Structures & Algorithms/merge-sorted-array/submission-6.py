class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        
        i=0
        j=0
        a=m+n
        while i<a and j<n:
            if i<m:
                if nums1[i]<nums2[j]:
                    i+=1
                else: 
                    #nums1[i]>=nums2[j]:
                    nums1[i+1:m+n]=nums1[i:m]
                    nums1[i]=nums2[j]
                    i+=1
                    j+=1
                    m+=1
            else:
                nums1[i:]=nums2[j:]
                return nums1
            


        #return nums1