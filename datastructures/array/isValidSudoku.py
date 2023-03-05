from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        vis = [[0 for _ in range(10)] for _ in range(9)]
        row = [[0 for _ in range(10)] for _ in range(9)]
        col = [[0 for _ in range(10)] for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                num = int(board[i][j])
                if vis[i // 3 + (j // 3) * 3][num] or row[i][num] or col[j][num]:
                    return False
                vis[i // 3 + j // 3 * 3][num] = 1
                row[i][num] = 1
                col[j][num] = 1

        return True


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
print(Solution().isValidSudoku(board))
