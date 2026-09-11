import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        freqTable = defaultdict(int)
        for task in tasks:
            freqTable[task] += 1
        q = []
        for key in freqTable:
            heapq.heappush(q, -1 * freqTable[key])
        answer = 0
        while q:
            
            previous = []
            increment = 0
            for _ in range(n + 1):
                if not q:
                    if len(previous) > 0:
                        increment = n + 1                    
                    break
                popped = heapq.heappop(q)
                if popped + 1 != 0:
                    previous.append(popped + 1)
                increment += 1
            answer += increment
            for prev in previous:
                heapq.heappush(q, prev)
        return answer