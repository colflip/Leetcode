# 1254. 统计封闭岛屿的数目

class Solution:
    def closedIsland(self, grid) -> int:
        def fun(x, y):
            if grid[x][y] == 0:
                grid[x][y] = 1
                if x + 1 < len(grid): fun(x + 1, y)
                if x - 1 >= 0: fun(x - 1, y)
                if y + 1 < len(grid[0]): fun(x, y + 1)
                if y - 1 >= 0: fun(x, y - 1)

        for x in range(len(grid)):
            fun(x, 0)
            fun(x, len(grid[0]) - 1)
        for y in range(len(grid[0])):
            fun(0, y)
            fun(len(grid) - 1, y)
        res = 0
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == 0:
                    fun(x, y)
                    res += 1
        return res


grid = [[1, 1, 1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 0]]
print(Solution().closedIsland(grid))
