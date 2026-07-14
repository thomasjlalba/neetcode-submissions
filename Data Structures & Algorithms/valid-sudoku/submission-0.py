class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hor = [set() for _ in range(9)]
        ver = [set() for _ in range(9)]
        square = [set() for _ in range(9)]

        for row in range(len(board)):
            for col, cell in enumerate(board[row]):
                if cell == ".":
                    continue
                squarePosn = (col // 3) + (row // 3) * 3
                if cell in hor[row] or cell in ver[col] or cell in square[squarePosn]:
                    # print(cell)
                    # print(row)
                    # print(col)
                    # print(hor[row])
                    # print(ver[col])
                    # print(square[squarePosn])
                    return False
                # update them all
                hor[row].add(cell)
                ver[col].add(cell)
                square[squarePosn].add(cell)
        return True
