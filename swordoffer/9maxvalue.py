# 47. 礼物的最大价值

class Solution:
    def maxValue(self, grid) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    continue
                elif i == 0 and j != 0:
                    grid[i][j] += grid[i][j - 1]
                elif i != 0 and j == 0:
                    grid[i][j] += grid[i - 1][j]
                else:
                    grid[i][j] += max(grid[i][j - 1], grid[i - 1][j])
        return grid[-1][-1]


grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
print(Solution().maxValue(grid))
