# 200. 岛屿数量

class Solution:
    def numIslands(self, grid) -> int:
        self.grid = grid
        self.ans = 0
        self.height = len(grid)
        self.width = len(grid[0])

        for i in range(self.height):
            for j in range(self.width):
                if self.grid[i][j] == '1':
                    self.ans += 1
                    self.dfs(i, j)
        return self.ans

    def dfs(self, i, j):
        self.grid[i][j] = '0'
        if j + 1 < self.width and self.grid[i][j + 1] == '1':
            self.dfs(i, j + 1)
        if j - 1 >= 0 and self.grid[i][j - 1] == '1':
            self.dfs(i, j - 1)
        if i + 1 < self.height and self.grid[i + 1][j] == '1':
            self.dfs(i + 1, j)
        if i - 1 >= 0 and self.grid[i - 1][j] == '1':
            self.dfs(i - 1, j)


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
print(Solution().numIslands(grid))
