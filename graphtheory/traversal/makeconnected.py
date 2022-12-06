# 1319. 连通网络的操作次数

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        times = 0
        vist = {}
        graph = {}
        for i in range(n):
            graph[i] = {}
        for j in connections:
            graph[j[0]][j[1]] = 1
            graph[j[1]][j[0]] = 1

        def dfs(i):
            vist[i] = 1
            for j in graph[i].keys():
                if j not in vist:
                    dfs(j)

        for i in range(n):
            if i not in vist.keys():
                dfs(i)
                times += 1
        return -1 if len(connections) < n - 1 else times - 1
