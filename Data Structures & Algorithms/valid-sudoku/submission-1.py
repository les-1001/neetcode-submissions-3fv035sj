class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # store seen values using dict(set)

        col = defaultdict(set)
        row = defaultdict(set)
        square = defaultdict(set)

        # parse through every box to find dupicates

        for r in range(9):
            for c in range(9):
                find = board[r][c]
                if find == ".":
                    continue
                if find in row[r] or find in col[c] or find in square[(r//3, c//3)]:
                    return False
                row[r].add(find)
                col[c].add(find)
                square[(r//3, c//3)].add(find)

        return True