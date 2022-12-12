# 886. 可能的二分法
import collections
import functools
from typing import List


class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for s, e in dislikes:
            graph[s].append(e)
            graph[e].append(s)
        group = dict()

        @functools.lru_cache(None)
        def dfs(i, g=1):
            if i in group:
                return group[i] == g
            group[i] = g
            for con in graph[i]:
                if not dfs(con, -1 * g):
                    return False
            return True

        for i in range(1, N + 1):
            if i not in group and not dfs(i):
                return False
        return True


if __name__ == "__main__":
    n = 4
    dislikes = [[1, 2], [1, 3], [2, 4]]
    print(Solution().possibleBipartition(n, dislikes))
