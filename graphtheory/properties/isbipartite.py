# 785. 判断二分图
from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        visited = [-1] * n
        for i in range(n):
            if visited[i] == -1:
                if not self.dfs(graph, i, 0, visited):
                    return False
        return True

    def dfs(self, graph, v, color, visited):
        visited[v] = color
        for i in graph[v]:
            if visited[i] == -1:
                if not self.dfs(graph, i, 1 - color, visited):
                    return False
            elif visited[i] == color:
                return False
        return True


if __name__ == "__main__":
    graph = [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
    print(Solution().isBipartite(graph))
