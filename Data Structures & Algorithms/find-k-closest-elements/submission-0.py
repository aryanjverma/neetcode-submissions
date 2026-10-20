import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        q = []
        for num in arr:
            print(num)
            heapq.heappush(q, (abs(num - x), num))
            
        answer = []
        print(q)
        for _ in range(k):
            answer.append(heapq.heappop(q)[1])
        answer.sort()
        return answer