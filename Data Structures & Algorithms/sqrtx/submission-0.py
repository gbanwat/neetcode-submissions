class Solution:
    def mySqrt(self, x: int) -> int:
        l=1
        r=x

        while l<=r:
            m=(l+r)//2
            m_sq=m*m
            if m_sq>x:
                r=m-1
            elif m_sq<x:
                l=m+1
            else:
                return m
        return int((l+r)/2)
        