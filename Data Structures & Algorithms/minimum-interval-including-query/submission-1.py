import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        queries = [(queries[i], i) for i in range(len(queries))]
        queries.sort(key=lambda x: x[0])
        intervals.sort()
        answer = [-1] * len(queries)
        q = []
        j = 0
        
        for i in range(len(queries)):
            query, index = queries[i]
            while j < len(intervals) and query >= intervals[j][0]:
                heapq.heappush(q, ((1 + intervals[j][1] - intervals[j][0]), intervals[j][1]))
                j += 1
            if len(q) > 0:
            
                length, end = heapq.heappop(q)
                if end >= query:
                    heapq.heappush(q, (length, end))
                    answer[index] = length
                else:
                    while len(q) > 0 and end < query:
                        length, end = heapq.heappop(q)
                        if end >= query:
                            heapq.heappush(q, (length, end))
                            answer[index] = length
                            break
        return answer