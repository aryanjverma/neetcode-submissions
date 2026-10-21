class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = float('inf')
        right = 0
        for weight in weights:
            right += weight
            left = min(left, weight)
        
        def isValid(val):
            index = 0
            d = 0
            count = 0
            while index < len(weights):
                if d == days:
                    return False
                while index < len(weights):
                    if count + weights[index] > val:
                        d += 1
                        count = 0
                        break
                    count += weights[index]
                    index += 1
            return True

        best = float('inf')
        while left <= right:
            mid = (left + right) // 2
            if isValid(mid):
                best = min(best, mid)
                right = mid - 1
            else:
                left = mid + 1
        return best
