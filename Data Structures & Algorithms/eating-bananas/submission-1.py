import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        answer = float('inf')
        while left <= right:
            mid = (left + right) // 2

            time = 0

            for pile in piles:
                time += (math.ceil(pile / mid))
                if time > h:
                    break
            if time > h:
                left = mid + 1
            else:
                answer = min(answer, mid)
                right = mid - 1
        return answer