"""
add-binary
https://leetcode-cn.com/problems/add-binary/
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        x, y = int(a, 2), int(b, 2)
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
        return bin(x)[2:]


if __name__ == "__main__":
    a = "1010"
    b = "1011"
    s = Solution()
    print(s.addBinary(a, b))
