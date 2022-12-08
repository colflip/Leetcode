# 847. 访问所有节点的最短路径
from collections import deque


class Solution:
    def shortestPathLength(self, graph) -> int:
        n = len(graph)
        queue = deque([(i, 1 << i, 0) for i in range(n)])
        visited = {(i, 1 << i) for i in range(n)}
        while queue:
            index, status, path = queue.popleft()
            if status == ((1 << n) - 1):
                return path
            for next_index in graph[index]:
                next_status = status | (1 << next_index)
                if (next_index, next_status) not in visited:
                    queue.append((next_index, next_status, path + 1))
                    visited.add((next_index, next_status))
        return -1


graph = [[1, 2, 3], [0], [0], [0]]
print(Solution().shortestPathLength(graph))
