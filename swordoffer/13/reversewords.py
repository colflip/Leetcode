# 剑指 Offer 58 - I. 翻转单词顺序

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])


s = "the sky is blue"
print(Solution().reverseWords(s))
