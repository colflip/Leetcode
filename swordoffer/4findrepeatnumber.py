# 03. 数组中重复的数字
# （1）排序 （2）map （3）桶计数 （4）位置重复


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:

        dict = {}
        for i in nums:
            if i in dict:
                return i
            else:
                dict[i] = 1
        return -1


nums = [2, 3, 1, 0, 2, 5, 3]
print(Solution().findRepeatNumber(nums))
