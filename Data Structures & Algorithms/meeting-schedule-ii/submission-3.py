"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        q = []
        maxLength = 0
        intervals.sort(key = lambda x: x.start)
        for interval in intervals:
            pair = (interval.end, interval.start)
            
            while q and q[0][0] <= pair[1]:
                heapq.heappop(q)
            
            heapq.heappush(q, pair)
            maxLength = max(maxLength, len(q))
        return maxLength
