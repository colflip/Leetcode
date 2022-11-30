# 695. 岛屿的最大面积

class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        n = len(grid)
        m = len(grid[0])
        res = 0

        def dfs(row, colum):
            if row < 0 or colum < 0 or row == n or colum == m or grid[row][colum] != 1:
                return 0
            grid[row][colum] = 0
            return dfs(row + 1, colum) + dfs(row - 1, colum) + dfs(row, colum - 1) + dfs(row, colum + 1) + 1

        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    res = max(dfs(i, j), res)
        return res


grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
print(Solution().maxAreaOfIsland(grid))
