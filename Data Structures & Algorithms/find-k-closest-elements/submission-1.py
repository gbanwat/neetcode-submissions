class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l=0
        for r in range(k,len(arr)):
            if abs((arr[r]-x))<abs((arr[l]-x)):
                l+=1
        return arr[l:l+k]



        