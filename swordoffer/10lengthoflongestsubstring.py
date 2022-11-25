# 48.最长不含重复字符的子字符串

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        res = temp = 0
        for j in range(len(s)):
            i = dic.get(s[j], -1)
            dic[s[j]] = j
            temp = temp + 1 if temp < j - i else j - i
            res = max(res, temp)
        return res


s = "abcabcbb"
print(Solution().lengthOfLongestSubstring(s))
