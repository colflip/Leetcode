import bisect
from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        q = []
        res = 0
        for v in nums:
            i = bisect.bisect_left(q, -v)
            res += i
            q[i:i] = [-v]
        return res


nums = [7, 5, 6, 4]
print(Solution().reversePairs(nums))
