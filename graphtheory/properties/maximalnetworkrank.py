# 1615. 最大网络秩
from typing import List


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        cnts = [0] * n
        has = [[0] * n for _ in range(n)]
        for i, j in roads:
            has[i][j] = 1
            has[j][i] = 1
            cnts[i] += 1
            cnts[j] += 1
        return max(cnts[i] + cnts[j] - has[i][j] for i in range(n) for j in range(i + 1, n))
