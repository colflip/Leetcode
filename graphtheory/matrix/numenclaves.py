# 1020. 飞地的数量

class Solution:
    def dfs(self, grid, i, j, visited):
        global res
        m, n = len(grid), len(grid[0])
        if i < 0 or j < 0 or i > m - 1 or j > n - 1: return
        direct = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        if visited[i][j] or grid[i][j] == 0: return
        visited[i][j] = 1
        res += 1
        for dir_ in direct:
            self.dfs(grid, i + dir_[0], j + dir_[1], visited)

    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[0] * n for _ in range(m)]
        global res
        res = 0
        for i in range(m):
            self.dfs(grid, i, 0, visited)
            self.dfs(grid, i, n - 1, visited)
        for j in range(n):
            self.dfs(grid, 0, j, visited)
            self.dfs(grid, m - 1, j, visited)
        res = 0
        for i in range(m):
            for j in range(n):
                if visited[i][j] or grid[i][j] == 0:
                    continue
                else:
                    self.dfs(grid, i, j, visited)
        return res
