import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        pending = []
        available = []
        answer = []
        time = 0
        for i in range(len(tasks)):
            task = tasks[i]
            heapq.heappush(pending, (task[0], task[1], i))
        while pending or available:
            while pending and pending[0][0] <= time:
                start, length, index = heapq.heappop(pending)
                heapq.heappush(available, (length, index))
            
            if available:
                length, index = heapq.heappop(available)
                time += length
                answer.append(index)
            else:
                time = pending[0][0]
        return answer