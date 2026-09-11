import heapq
class MedianFinder:

    def __init__(self):
        self.lowerHeap = []
        self.upperHeap = []
        self.size = 0
    def addNum(self, num: int) -> None:
        self.size += 1
        if len(self.lowerHeap) < len(self.upperHeap):
            if self.upperHeap and self.upperHeap[0] < num:
                heapq.heappush(self.lowerHeap, -1 * heapq.heappop(self.upperHeap))
                heapq.heappush(self.upperHeap, num)
            else:
                heapq.heappush(self.lowerHeap, -1 * num)
        else:
            if self.lowerHeap and self.lowerHeap[0] * -1 >= num:
                heapq.heappush(self.upperHeap, -1 * heapq.heappop(self.lowerHeap))
                heapq.heappush(self.lowerHeap, -1 * num)
            else:
                heapq.heappush(self.upperHeap, num)
    def findMedian(self) -> float:
        
        if self.size % 2 == 1:
            return self.upperHeap[0]
        else:
            return (self.upperHeap[0] + -1 * self.lowerHeap[0]) / 2