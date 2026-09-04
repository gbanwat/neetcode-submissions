class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)

        res=r

        while l<=r:
            m=(l+r)//2
            time=0
            time+=sum((p+m-1)//m for p in piles)

            if time>h:
                l=m+1
            elif time<=h:
                r=m-1
                res=min(res,m)
        return res

        