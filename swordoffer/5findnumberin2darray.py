# 04. 二维数组中的查找
# 站在矩阵右上角看

class Solution:
    def findNumberIn2DArray(self, matrix, target: int) -> bool:
        if not matrix:
            return False
        self.res = False
        self.target = target
        self.helper(0, len(matrix[0]) - 1, matrix)
        return self.res

    def helper(self, i, j, matrix):
        if i < len(matrix) and j >= 0:
            if matrix[i][j] == self.target:
                self.res = True
            if matrix[i][j] > self.target:
                self.helper(i, j - 1, matrix)
            else:
                self.helper(i + 1, j, matrix)
