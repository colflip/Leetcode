# 1091. 二进制矩阵中的最短路径

import collections


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        l = len(grid)
        if grid[0][0] != 0 or grid[l - 1][l - 1] != 0:
            return -1
        if l == 1:
            return 1

        visited = set((0, 0))
        Q = collections.deque([(0, 0)])
        Q2 = collections.deque([])
        ans = 0

        while Q:
            ans += 1
            while Q:
                i, j = Q.popleft()
                if i == l - 1 and j == l - 1:
                    return ans
                for (x, y) in [(i - 1, j), (i + 1, j), (i, j + 1), (i, j - 1), (i + 1, j + 1), (i + 1, j - 1),
                               (i - 1, j + 1), (i - 1, j - 1)]:
                    if (x, y) not in visited and l > x >= 0 and l > y >= 0:
                        if grid[x][y] == 0:
                            visited.add((x, y))
                            Q2.append((x, y))
            while Q2:
                Q.append(Q2.popleft())
        return -1
