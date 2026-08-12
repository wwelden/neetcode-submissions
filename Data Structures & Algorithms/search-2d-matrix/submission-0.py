class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t, b = 0, len(matrix) -1
        w = len(matrix[0]) -1
        l, r = 0, w

        

        while t <= b:
            m = t + ((b - t) // 2)
            if matrix[m][0] > target:
                b = m - 1
            elif matrix[m][w] < target:
                t = m + 1
            else: 
                while l <= r:
                    mid = l + ((r - l) // 2)
                    if matrix[m][mid] > target:
                        r = mid -1
                    elif matrix[m][mid] < target:
                        l = mid + 1
                    else: 
                        return True
                return False
        return False
        

   