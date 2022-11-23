# 10- I. 斐波那契数列
'''
模块lru_cache: 记录以往函数运行的结果，它把耗时的函数的结果保存起来方便下次使用，实现了备忘功能，它在递归函数中有着非常明显的效果。
https://blog.csdn.net/weixin_44430893/article/details/120860433
-----------------------
为什么要对1000000007取模（取余）
1000000007是一个质数（素数），对质数取余能最大程度避免冲突～
https://www.liuchuo.net/archives/645
'''

from functools import lru_cache


class Solution:
    @lru_cache(None)
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        return (self.fib(n - 1) + self.fib(n - 2)) % 1000000007


n = 37
print(Solution().fib(n))
