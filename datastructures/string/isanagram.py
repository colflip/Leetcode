# 242. 有效的字母异位词
import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        couter = collections.Counter(s)
        for i in t:
            if i not in couter:
                return False
            couter[i] -= 1
            if couter[i] < 0:
                return False
        return True

    def isAnagram2(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


s = "anagram"
t = "nagaram"
print(Solution().isAnagram(s, t))

s = "rat"
t = "car"
print(Solution().isAnagram(s, t))
