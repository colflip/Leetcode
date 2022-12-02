# 剑指 Offer 41. 数据流中的中位数

from heapq import *


class MedianFinder:
    def __init__(self):
        self.big_heap = []
        self.sml_heap = []

    def addNum(self, num: int) -> None:
        if len(self.big_heap) != len(self.sml_heap):
            heappush(self.big_heap, -heappushpop(self.sml_heap, -num))
        else:
            heappush(self.sml_heap, -heappushpop(self.big_heap, num))

    def findMedian(self) -> float:
        return -self.sml_heap[0] if len(self.big_heap) != len(self.sml_heap) else (self.big_heap[0] - self.sml_heap[
            0]) / 2.0
