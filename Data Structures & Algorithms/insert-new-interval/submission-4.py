class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        if newInterval[1] < intervals[0][0]:
            intervals.insert(0, newInterval)
            return intervals
        for i in range(len(intervals)):
            interval = intervals[i]
            if interval[1] >= newInterval[0]:
                interval[0] = min(interval[0], newInterval[0])
                interval[1] = max(interval[1], newInterval[1])
                break
            elif interval[1] < newInterval[0] and (i == len(intervals) - 1 or intervals[i + 1][0] > newInterval[1]):
                intervals.insert(i + 1, newInterval)
                
                return intervals
        
        answer = []
        answer.append(intervals[0])
        for j in range(len(intervals)):
            if answer[-1][1] >= intervals[j][0]:
                answer[-1][1] = max(intervals[j][1], answer[-1][1])
            else:
                answer.append(intervals[j])
        return answer