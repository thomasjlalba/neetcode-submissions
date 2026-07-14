func isValidSudoku(board [][]byte) bool {
    hor, ver, square := make([]int, 9), make([]int, 9), make([]int, 9)

    for r, row := range board {
        for c, cell := range row {
            if cell == '.' {
                continue
            }
            bit := 1 << (cell - '1')
            squarePosn := (c / 3) + (r / 3) * 3
            if (hor[c] & bit) != 0 || (ver[r] & bit) != 0 || (square[squarePosn] & bit) != 0 {
                return false
            }
            hor[c] |= bit
            ver[r] |= bit
            square[squarePosn] |= bit
        }
    }
    return true
}
