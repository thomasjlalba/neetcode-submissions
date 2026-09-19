func searchMatrix(matrix [][]int, target int) bool {
    lr, rr := 0, len(matrix) - 1
    for lr < rr {
        mid := lr + rr
        if mid % 2 == 0 {
            mid /= 2
        } else {
            mid = (mid + 1) / 2 
        }
        if matrix[mid][0] == target {
            return true
        }
        if matrix[mid][0] > target {
            rr = mid - 1
        } else {
            lr = mid
        }
    }
    lc, rc := 0, len(matrix[0]) - 1
    for lc <= rc {
        mid := (lc + rc) / 2
        if matrix[lr][mid] == target {
            return true
        }
        if matrix[lr][mid] > target {
            rc = mid - 1
        } else {
            lc = mid + 1
        }
    }
    return false
}
