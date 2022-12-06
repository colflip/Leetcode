# 547. 省份数量

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        candidates = set(range(1, len(isConnected)))
        if not candidates:
            return 1
        count = 0
        peoples = [0]
        while candidates:
            while peoples:
                people = peoples.pop()
                friends = [i for i in candidates if isConnected[people][i]]
                for i in friends:
                    peoples.append(i)
                    candidates.remove(i)
            count += 1
            if candidates:
                peoples = [list(candidates)[0]]
        return count
