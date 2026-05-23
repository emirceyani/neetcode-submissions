class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, h = 0, (len(matrix[0])*len(matrix)) -1
        while l <= h:
            m = (l + h) //2
            r,c = m //len(matrix[0]), m % len(matrix[0])
            if target > matrix[r][c]:
                l = m +1
            elif target < matrix[r][c]:
                h = m-1
            else:
                return True
        return False