class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lr, rr = 0, len(matrix) - 1
        while lr < rr:
            mid = math.ceil((lr + rr) / 2)
            if matrix[mid][0] == target:
                return True
            if matrix[mid][0] > target:
                rr = mid - 1
            else:
                lr = mid
        
        # it will be in row lr / rr if it exists
        lc, rc = 0, len(matrix[0]) - 1
        while lc < rc:
            mid = (lc + rc) // 2
            if matrix[lr][mid] == target:
                return True
            if matrix[lr][mid] > target:
                rc = mid - 1
            else:
                lc = mid + 1
        if matrix[lr][lc] == target:
            return True
        return False