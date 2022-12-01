# 面试题13. 机器人的运动范围

class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def count_int(num: int):
            cnt = 0
            for s in str(num):
                cnt += int(s)
            return cnt
        visit_cnt = set()
        queue = deque([(0, 0)])
        while queue:
            node = queue.popleft()
            if node in visit_cnt:
                continue
            else:
                visit_cnt.add(node)
            i, j = node[0], node[1]
            if i + 1 < m and count_int(i + 1) + count_int(j) <= k:
                queue.append((i + 1, j))
            if j + 1 < n and count_int(i) + count_int(j + 1) <= k:
                queue.append((i, j + 1))
        return len(visit_cnt)
