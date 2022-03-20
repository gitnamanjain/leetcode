class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        targetin=0
        for i in range(len(matrix)):
            leny=len(matrix[i])-1
            if(target<=matrix[i][leny]):
                targetin=i
                break
        
        for j in (matrix[targetin]):
            if(j==target):
                return True
        return False