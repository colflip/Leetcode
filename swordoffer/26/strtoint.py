# 面试题67. 把字符串转换成整数
import re


class Solution:
    def strToInt(self, str: str) -> int:
        mystr = re.findall('^[\+\-]?[\d]+', str.strip())
        if len(mystr) == 0:
            mynum = 0
        else:
            mynum = int(mystr[0])
        if mynum > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif mynum < -2 ** 31:
            return -2 ** 31
        else:
            return mynum


if __name__ == '__main__':
    str = "4193 with words"
    print(Solution().strToInt(str))
