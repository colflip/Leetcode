# 1466. 重新规划路线

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        p1, p2 = [[] for i in range(n)], [[] for i in range(n)]
        st = [False] * n

        def bfs() -> int:
            res = 0
            q = [0]
            st[0] = True
            while len(q):
                front = q[0]
                for e in p1[front]:
                    if not st[e]:
                        st[e] = True
                        q.append(e)
                        res += 1
                for e in p2[front]:
                    if not st[e]:
                        st[e] = True
                        q.append(e)
                q = q[1:]
            return res

        for e in connections:
            p1[e[0]].append(e[1])
            p2[e[1]].append(e[0])
        return bfs()
