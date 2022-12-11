# 997. 找到小镇的法官
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        a = [0 for x in range(n + 1)]
        b = [0 for x in range(n + 1)]

        for num in trust:
            a[num[1]] += 1
            b[num[0]] += 1

        for i, num in enumerate(a):
            if i != 0 and num == n - 1:
                if b[i] == 0:
                    return i
        return -1


n, trust = 3, [[1, 3], [2, 3], [3, 1]]
print(Solution().findJudge(n, trust))
