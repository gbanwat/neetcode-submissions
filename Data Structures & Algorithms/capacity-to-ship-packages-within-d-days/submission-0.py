class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def canship(cap):
            n_ships=1
            t_wt=0
            for w in weights:
                t_wt+=w
                if t_wt>cap:
                    n_ships+=1
                    t_wt=w
            if n_ships<=days:
                return True
            else:
                return False

        l=max(weights)
        r=sum(weights)

        res=sum(weights)
        while l<=r:
            m=(l+r)//2
            if canship(m):
                r=m-1
                res=min(res,m)
            else:
                l=m+1
        return res

        