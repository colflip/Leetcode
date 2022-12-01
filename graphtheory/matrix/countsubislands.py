# 1905. 统计子岛屿

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def floodFill(x, y):
            if x < 0 or x >= n or y < 0 or y >= m or not grid2[x][y]: return True
            grid2[x][y] = 0
            return floodFill(x - 1, y) & floodFill(x + 1, y) & floodFill(x, y - 1) & floodFill(x, y + 1) & grid1[x][y]
        n, m = len(grid1), len(grid1[0])
        return sum(floodFill(i, j) for i in range(n) for j in range(m) if grid2[i][j])