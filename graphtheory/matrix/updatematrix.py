# 542. 01 矩阵

import collections


class Solution:
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(matrix), len(matrix[0])
        Q = collections.deque([])
        visited = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    Q.append((i, j))
                    visited.add((i, j))
        while Q:
            i, j = Q.popleft()
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < m and 0 <= y < n and (x, y) not in visited:
                    matrix[x][y] = matrix[i][j] + 1
                    visited.add((x, y))
                    Q.append((x, y))
        return matrix
