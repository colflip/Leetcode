# 1376. 通知所有员工所需的时间

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        path, root = [[] for i in range(n)], -1
        for i in range(n):
            if manager[i] == -1:
                root = i
            else:
                path[manager[i]].append(i)
        ans = 0
        lis = [[root, 0]]
        for i in range(n):
            a = lis[i]
            if len(path[a[0]]) > 0:
                ans = max(ans, a[1] + informTime[a[0]])
            for b in path[a[0]]:
                lis.append([b, a[1] + informTime[a[0]]])
        return ans
