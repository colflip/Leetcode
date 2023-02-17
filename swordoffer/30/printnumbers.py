from typing import List


class Solution:
    def printNumbers(self, n: int) -> List[int]:
        out_list = list()
        for i in range(1, 10 ** n):
            out_list.append(i)
        return out_list


n = 1
print(Solution().printNumbers(n))
