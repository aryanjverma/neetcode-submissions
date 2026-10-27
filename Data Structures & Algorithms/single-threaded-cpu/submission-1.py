import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        q = []
        for i in range(len(tasks)):
            task = tasks[i]
            heapq.heappush(q, (task[0], task[1], i))
        start, length, index = heapq.heappop(q)
        ending = start + length
        answer = [index]
        while q:
            newQ = []
            while q and ending >= q[0][0]:
                popped = heapq.heappop(q)
                heapq.heappush(newQ, (popped[1], popped[2]))
            if newQ:
                length, index = heapq.heappop(newQ)
                answer.append(index)
                ending += length
                while newQ:
                    popped = heapq.heappop(newQ)
                    heapq.heappush(q, (ending, popped[0], popped[1]))
            else:
                start, length, index = heapq.heappop(q)
                answer.append(index)
                ending = start + length
        return answer