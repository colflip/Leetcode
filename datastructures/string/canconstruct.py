# 383. 赎金信
import collections


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = collections.Counter(magazine)
        for ch in ransomNote:
            if ch not in count or count[ch] <= 0:
                return False
            count[ch] -= 1
        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.canConstruct("a", "b"))
    print(solution.canConstruct("aa", "ab"))
    print(solution.canConstruct("aa", "aab"))
