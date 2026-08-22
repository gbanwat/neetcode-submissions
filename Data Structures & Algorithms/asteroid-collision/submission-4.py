class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res=[]

        for r in asteroids:
            if len(res)==0:
                res.append(r)
            else:
                #l=res.pop()

                while len(res)>0:
                    l=res.pop()

                    if abs(l)==l and abs(r)!=r:
                        if abs(l)>abs(r):
                            res.append(l)
                            break
                        elif abs(l)==abs(r):
                            break
                        else:
                            if len(res)==0:
                                res.append(r)
                                break
                            else:
                                continue
                        
                    else:
                        res.append(l)
                        res.append(r)
                        break
        return res


        


                