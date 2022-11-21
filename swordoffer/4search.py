# 3 - I. 在排序数组中查找数字 I

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        R = right

        if R < 0 or nums[R] != target:
            return 0
        left = 0
        right = R
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        L = left
        return R - L + 1

        # -----------------------
        # d=0
        # for i in nums:
        #     if target==i:
        #         d=d+1
        # return d


nums = [5, 7, 7, 8, 8, 10]
target = 7
print(Solution().search(nums, target))
