from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        records = dict()
        for idx, val in enumerate(nums):
            if target - val not in records:
                records[val] = idx
            else:
                return [records[target - val], idx]


nums = [2, 7, 11, 15]
target = 9
print(Solution().twoSum(nums, target))
