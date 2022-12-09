# 1306. 跳跃游戏 III
# https://leetcode-cn.com/problems/jump-game-iii/

from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        seen = set()
        queue = [(start, 0)]
        while queue:
            index, step = queue.pop(0)
            if index in seen:
                continue
            seen.add(index)
            if index < 0 or index >= len(arr):
                continue
            if arr[index] == 0:
                return True
            queue.extend([(index + arr[index], step + 1), (index - arr[index], step + 1)])
        return False


if __name__ == "__main__":
    solution = Solution()
    arr = [4, 2, 3, 0, 3, 1, 2]
    start = 5
    print(solution.canReach(arr, start))
