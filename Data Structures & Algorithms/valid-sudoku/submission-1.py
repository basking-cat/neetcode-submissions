from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(0,9):
            for c in range(0,9):
                cur = board[r][c]
                if cur == '.':
                    continue

                box_key = (r//3, c//3)
                if cur in rows[r] or cur in cols[c] or cur in boxes[box_key]:
                    return False
                
                rows[r].add(cur)
                cols[c].add(cur)
                boxes[box_key].add(cur)

        return True

    # t: O(1) (O(n^2) where n = 9 )
    # s: O(1) (O(n^2) where n = 9 )