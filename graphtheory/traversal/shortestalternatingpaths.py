# 1129. 颜色交替的最短路径


class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        dist = [1e9] * 2 * n

        graph = [[] for _ in range(2 * n)]
        for u, v in redEdges:
            graph[u].append(v + n)
        for u, v in blueEdges:
            graph[u + n].append(v)

        q = [0, n]
        dist[0] = dist[n] = 0
        while len(q) > 0:
            u = q[0]
            q = q[1:]
            for v in graph[u]:
                if dist[u] + 1 < dist[v]:
                    dist[v] = dist[u] + 1
                    q.append(v)

        answer = [min(dist[u], dist[u + n]) for u in range(n)]
        answer = [-1 if a == 1e9 else a for a in answer]

        return answer
