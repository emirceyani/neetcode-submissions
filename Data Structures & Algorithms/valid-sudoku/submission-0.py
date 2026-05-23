class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)
        #Row check

        #Column check

        #Squares check
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                n = board[r][c]
                if n in rows[r]:
                    return False
                if n in cols[c]:
                    return False
                if n in squares[(r//3, c//3)]:
                    return False
                cols[c].add(n)
                rows[r].add(n)
                squares[(r//3, c//3)].add(n)
        return True
