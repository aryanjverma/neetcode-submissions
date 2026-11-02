import heapq
from collections import deque
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        q = []
        for people, f, t in trips:
            heapq.heappush(q, (f, t, people))
        
        currPeople = deque()
        
        while q:
            if not currPeople:
                start, end, people = heapq.heappop(q)
                totalPeople = people
                if totalPeople > capacity:
                    return False
                currPeople.append((start, end, people))
            while q and currPeople[0][1] > q[0][0]:
                start, end, people = heapq.heappop(q)
                if currPeople[-1][1] <= start:
                    totalPeople -= currPeople.popleft()[2]
                totalPeople += people
                if totalPeople > capacity:
                    return False
                currPeople.append((start, end, people))
            totalPeople -= currPeople.popleft()[2]
        return True
