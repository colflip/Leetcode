# 剑指 Offer 05. 替换空格

class Solution:
    def replaceSpace(self, s: str) -> str:
        return s.replace(" ", "%20")


s = "We are happy."
sol = Solution()
print(sol.replaceSpace(s))
