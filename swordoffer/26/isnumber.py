# 剑指 Offer 20. 表示数值的字符串
import re


class Solution:
    def isNumber(self, s: str) -> bool:
        def integer(c):
            if not c:
                return False
            cnt = c.count('.')
            if cnt > 0:
                return False
            else:
                return c.isdigit() if c[0] not in {'+', '-'} else c[1:].isdigit()

        def decimal(c):
            if not c:
                return False
            c = c if c[0] not in {'+', '-'} else c[1:]
            cnt = c.count('.')
            if cnt != 1:
                return False
            else:
                if len(c) == 1:
                    return False
                for num in re.split('\.', c):
                    if num:
                        if not num.isdigit():
                            return False
            return True

        if not s:
            return False
        s = s.strip()
        cnt = len(re.findall('e|E', s))
        if cnt > 1:
            return False
        elif cnt == 0:
            return integer(s) or decimal(s)
        elif cnt == 1:
            nums = re.split('e|E', s)
            return (integer(nums[0]) or decimal(nums[0])) and integer(nums[-1])
