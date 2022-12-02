# 417. 太平洋大西洋水流问题
from collections import deque


class Solution:
    def pacificAtlantic(self, heights):
        m, n = len(heights), len(heights[0])
        po = [[False for _ in range(n)] for _ in range(m)]
        ao = [[False for _ in range(n)] for _ in range(m)]
        h = heights
        Qpo = deque([])
        Qao = deque([])
        for i in range(m):
            Qpo.append((i, 0))
            Qao.append((i, n - 1))

        for j in range(n):
            Qpo.append((0, j))
            Qao.append((m - 1, j))

        while Qpo:
            cx, cy = Qpo.popleft()
            po[cx][cy] = True
            for nx, ny in [(cx + 1, cy), (cx, cy + 1), (cx - 1, cy), (cx, cy - 1)]:
                if 0 <= nx < m and 0 <= ny < n and not po[nx][ny] and h[nx][ny] >= h[cx][cy]:
                    Qpo.append((nx, ny))

        while Qao:
            cx, cy = Qao.popleft()
            ao[cx][cy] = True
            for nx, ny in [(cx + 1, cy), (cx, cy + 1), (cx - 1, cy), (cx, cy - 1)]:
                if 0 <= nx < m and 0 <= ny < n and not ao[nx][ny] and h[nx][ny] >= h[cx][cy]:
                    Qao.append((nx, ny))

        ans = []
        for i in range(m):
            for j in range(n):
                if po[i][j] and ao[i][j]:
                    ans.append([i, j])
        return ans


heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
print(Solution().pacificAtlantic(heights))
