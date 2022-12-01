# 面试题45. 把数组排成最小的数

class Solution:
    def minNumber(self, nums) -> str:
        return ''.join(list(map(str, sorted(nums, key=lambda x: str(x) * 5))))