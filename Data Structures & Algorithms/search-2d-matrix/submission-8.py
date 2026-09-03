class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r=len(matrix)
        c=len(matrix[0]) if matrix else 0
        r_range=[]
        for r in range(len(matrix)):
            if c>1:
                r_range.append([matrix[r][0],matrix[r][-1]])
            else:
                r_range.append([matrix[r][0],matrix[r][0]+1])
        #return r_range
        
        for row in range(len(r_range)):
            #return r_range[row]
            if target in range(r_range[row][0],r_range[row][1]+1):
                row_num=row
                break
            else:
                row_num=0
        
        l=0
        r=len(matrix[row_num])-1

        while l<=r:
            m=(l+r)//2
            if target<matrix[row_num][m]:
                r=m-1
            elif target>matrix[row_num][m]:
                l=m+1
            else:
                return True
        return False

        