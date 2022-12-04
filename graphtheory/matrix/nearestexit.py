# 1926. 迷宫中离入口最近的出口

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        deq = [entrance]
        res = 0
        j1, j2 = len(maze), len(maze[0])
        maze[deq[0][0]][deq[0][1]] = '+'
        while deq:
            res += 1
            n = len(deq)
            for i in range(n):
                k1, k2 = deq[0][0], deq[0][1]
                del deq[0]
                if k1 < j1 - 1 and maze[k1 + 1][k2] == '.':
                    if k1 + 1 == j1 - 1 or k2 == 0 or k2 == j2 - 1:
                        return res
                    else:
                        deq.append([k1 + 1, k2])
                        maze[k1 + 1][k2] = '+'
                if k1 > 0 and maze[k1 - 1][k2] == '.':
                    if k1 - 1 == 0 or k2 == 0 or k2 == j2 - 1:
                        return res
                    else:
                        deq.append([k1 - 1, k2])
                        maze[k1 - 1][k2] = '+'
                if k2 < j2 - 1 and maze[k1][k2 + 1] == '.':
                    if k1 == j1 - 1 or k1 == 0 or k2 + 1 == j2 - 1:
                        return res
                    else:
                        deq.append([k1, k2 + 1])
                        maze[k1][k2 + 1] = '+'
                if k2 > 0 and maze[k1][k2 - 1] == '.':
                    if k1 == j1 - 1 or k1 == 0 or k2 - 1 == 0:
                        return res
                    else:
                        deq.append([k1, k2 - 1])
                        maze[k1][k2 - 1] = '+'
        return -1
