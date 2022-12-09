# 1654. 到家的最少跳跃次数
# https://leetcode-cn.com/problems/minimum-jumps-to-reach-home/
from collections import deque
from typing import List


class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        forbidden = set(forbidden)
        queue = deque()
        queue.append([0, 0, 0])
        if 0 in forbidden:
            return -1
        visited = set()
        right = 6000
        while queue:
            index, pre_dir, times = queue.popleft()
            if index > right:
                continue
            if index == x:
                return times
            if pre_dir:
                if (index + a) not in forbidden and (index + a) >= 0 and (index + a, 1) not in visited:
                    queue.append([index + a, 1, times + 1])
                    visited.add((index + a, 1))
                if (index - b) not in forbidden and (index - b) >= 0 and (index - b, 0) not in visited:
                    queue.append([index - b, 0, times + 1])
                    visited.add((index - b, 0))
            else:
                if (index + a) not in forbidden and (index + a) >= 0 and (index + a, 1) not in visited:
                    queue.append([index + a, 1, times + 1])
                    visited.add((index + a, 1))
        return -1


if __name__ == "__main__":
    solution = Solution()
    forbidden = [14, 4, 18, 1, 15]
    a = 3
    b = 15
    x = 9
    print(solution.minimumJumps(forbidden, a, b, x))
