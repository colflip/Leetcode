# 21. 调整数组顺序使奇数位于偶数前面

class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        q_list, o_list = [], []
        for i in nums:
            if i % 2 == 1:
                q_list.append(i)
            else:
                o_list.append(i)
        return q_list + o_list
