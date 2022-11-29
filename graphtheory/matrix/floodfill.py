# 733. 图像渲染

class Solution:
    def floodFill(self, image, sr: int, sc: int, newColor: int):
        def dfs(i, j, base, m, n):
            if 0 <= i < m and 0 <= j < n and image[i][j] == base:
                image[i][j] = newColor
                dfs(i + 1, j, base, m, n)
                dfs(i - 1, j, base, m, n)
                dfs(i, j + 1, base, m, n)
                dfs(i, j - 1, base, m, n)

        if image[sr][sc] != newColor:
            dfs(sr, sc, image[sr][sc], len(image), len(image[0]))
        return image


image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr, sc, newColor = 1, 1, 2
print(Solution().floodFill(image, sr, sc, newColor))
