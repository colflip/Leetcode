# 387. 字符串中的第一个唯一字符
import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)  # 统计每个字符出现的次数
        for i in range(len(s)):
            if count[s[i]] == 1:  # 找到第一个出现次数为1的字符
                return i
        return -1  # 未找到符合条件的字符，返回-1


if __name__ == "__main__":
    solution = Solution()
    print(solution.firstUniqChar("leetcode"))
    print(solution.firstUniqChar("loveleetcode"))
