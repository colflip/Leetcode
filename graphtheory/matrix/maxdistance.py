# 1162. 地图分析

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dis = [[float("inf") for j in range(m + 2)] for i in range(n + 2)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if grid[i - 1][j - 1]:
                    dis[i][j] = 0
                else:
                    dis[i][j] = min(dis[i - 1][j], dis[i][j - 1]) + 1
        res = -1
        for i in range(n, 0, -1):
            for j in range(m, 0, -1):
                if grid[i - 1][j - 1]:
                    dis[i][j] = 0
                else:
                    dis[i][j] = min(dis[i + 1][j] + 1, dis[i][j + 1] + 1, dis[i][j])
                    res = max(dis[i][j], res)
        return res if res != float("inf") else -1


grid = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
print(Solution().maxDistance(grid))
