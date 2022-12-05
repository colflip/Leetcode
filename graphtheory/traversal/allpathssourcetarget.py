# 797. 所有可能的路径

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        f = len(graph) - 1
        res = []

        def dfs(s, p):
            if s == f:
                res.append(p[:])
                return
            for x in graph[s]:
                p.append(x)
                dfs(x, p)
                p.pop()

        dfs(0, [0])
        return res
