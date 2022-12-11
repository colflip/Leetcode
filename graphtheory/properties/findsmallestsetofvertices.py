# 1557. 可以到达所有点的最少点数目
from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree = [0] * n
        for e in edges:
            indegree[e[1]] += 1
        return [i for i in range(n) if indegree[i] == 0]


if __name__ == "__main__":
    n, edges = 6, [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]
    print(Solution().findSmallestSetOfVertices(n, edges))
