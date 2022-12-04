# 934. 最短的桥

from collections import deque


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        q = deque()
        for si in range(m):
            for sj in range(n):
                if grid[si][sj] == 1:
                    q.append((si, sj, 0))
                    while q:
                        i, j, depth = q.popleft()
                        if grid[i][j] == -1:
                            continue
                        grid[i][j] = -1
                        for d in directions:
                            ni, nj = i + d[0], j + d[1]
                            if 0 <= ni < m and 0 <= nj < n:
                                if grid[ni][nj] == 0:
                                    q.append((ni, nj, depth + 1))
                                elif grid[ni][nj] == 1 and depth > 0:
                                    return depth
                                elif grid[ni][nj] == 1 and depth == 0:
                                    q.appendleft((ni, nj, depth))
