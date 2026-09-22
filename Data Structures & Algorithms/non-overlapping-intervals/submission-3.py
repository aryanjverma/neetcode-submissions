class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        removed = 0
        prevEnd = intervals[0][1]
        for i in range(1, len(intervals)):
            
            if prevEnd <= intervals[i][0]:
                prevEnd = intervals[i][1]
            else:
                prevEnd = min(intervals[i][1], prevEnd)
                removed += 1
        return removed