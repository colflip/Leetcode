from typing import List
from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = Counter(nums1)
        res = []
        for i in nums2:
            if i in nums1 and nums1[i]:
                res.append(i)
                nums1[i] -= 1
        return res


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(Solution().intersect(nums1, nums2))
