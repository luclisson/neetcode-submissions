class Solution:
    def helper(self, matrix,target, start, stop,n):
        if start>stop:
            return False
        
        mid = int(start + (stop - start) / 2)
        col = mid % n
        row = int(mid/n)

        if target == matrix[row][col]:
            return True
        
        if target > matrix[row][col]:
            return self.helper(matrix,target,mid+1,stop,n)
        else:
            return self.helper(matrix,target,start,mid-1,n)

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        m = len(matrix)
        n = len(matrix[0])
        return self.helper(matrix,target,0,n*m-1,n)
        
        