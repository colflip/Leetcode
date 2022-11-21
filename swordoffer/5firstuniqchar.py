# 50. 第一个只出现一次的字符
from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> str:
        counter = Counter(s)
        for i in s:
            if counter[i] == 1:
                return i
        return " "


s = "abaccdeff"
print(Solution().firstUniqChar(s))
