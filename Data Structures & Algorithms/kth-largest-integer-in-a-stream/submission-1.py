import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.q = nums
        heapq.heapify(self.q)
        self.k = k
        while (len(self.q) > k):
            heapq.heappop(self.q)

    def add(self, val: int) -> int:
        heapq.heappush(self.q, val)
        if len(self.q) > self.k:
            heapq.heappop(self.q)
        return self.q[0]
