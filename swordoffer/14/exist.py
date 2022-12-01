# 剑指 Offer 12. 矩阵中的路径

class Solution:
    def exist(self, board, word: str) -> bool:
        def dfs(board, i, j, word, k):
            if i < 0 or i == len(board) or j < 0 or j == len(board[0]):
                return False
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            board[i][j] = ''
            res = dfs(board, i - 1, j, word, k + 1) or dfs(board, i, j - 1, word, k + 1) \
                  or dfs(board, i + 1, j, word, k + 1) or dfs(board, i, j + 1, word, k + 1)
            board[i][j] = word[k]
            return res

        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                if dfs(board, i, j, word, 0):
                    return True
        return False
