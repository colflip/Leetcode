# 365. 水壶问题


class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        from collections import deque
        queue = deque([[0, 0]])
        visited = set([(0, 0)])
        while queue:
            cur_x, cur_y = queue.pop()
            if targetCapacity in [cur_x, cur_y, cur_x + cur_y]:
                return True
            for item in [(jug1Capacity, cur_y), (cur_x, jug2Capacity), (0, cur_y), (cur_x, 0),
                         (cur_x + cur_y - jug2Capacity, jug2Capacity) if cur_x + cur_y >= jug2Capacity else (
                         0, cur_x + cur_y),
                         (jug1Capacity, cur_x + cur_y - jug1Capacity) if cur_x + cur_y >= jug1Capacity else (
                         cur_x + cur_y, 0)]:
                if item not in visited:
                    queue.appendleft(item)
                    visited.add(item)
        return False

        # if targetCapacity == 0:
        #     return True
        # if jug1Capacity + jug2Capacity < targetCapacity:
        #     return False
        # if jug1Capacity > jug2Capacity:
        #     jug1Capacity, jug2Capacity = jug2Capacity, jug1Capacity
        # if jug1Capacity == 0:
        #     return jug2Capacity == targetCapacity
        # while jug2Capacity % jug1Capacity != 0:
        #     jug2Capacity, jug1Capacity = jug1Capacity, jug2Capacity % jug1Capacity
        # return targetCapacity % jug1Capacity == 0


if __name__ == '__main__':
    solution = Solution()
    jug1Capacity, jug2Capacity, targetCapacity = 3, 5, 4
    print(solution.canMeasureWater(jug1Capacity, jug2Capacity, targetCapacity))
