# 841. 钥匙和房间

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        stk = rooms[0]
        rooms[0] = []
        while stk:
            node = stk.pop()
            for v in rooms[node]:
                stk.extend(rooms[v])
                rooms[v].clear()
            rooms[node].clear()
        return not any(rooms)
