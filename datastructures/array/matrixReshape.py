from typing import List


class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(nums), len(nums[0])
        if m * n != r * c:
            return nums
        # 按行优先排列成一维数组
        arr = [0] * (m * n)
        index = 0
        for i in range(m):
            for j in range(n):
                arr[index] = nums[i][j]
                index += 1

        # 按照重塑矩阵的形状生成新的二维数组
        result = []
        for i in range(r):
            result.append(arr[i * c: (i + 1) * c])

        return result

nums =[[1,2],[3,4]]
r = 2
c = 4
print(Solution().matrixReshape(nums,r,c))