import math
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        if len(people) == 1:
            return 1
        w = limit * [0]
        count = 0
        for person in people:
            if person == limit:
                count += 1
            else:
                w[person] += 1
        l = 1
        r = limit - 1
        
        while l < r:
            while l < r and w[l] == 0:
                l += 1
            while l < r and w[r] == 0:
                r -= 1
            while l < r and l + r > limit:
                count += w[r]
                w[r] = 0
                r -= 1
                
            while l < r and w[r] > 0 and w[l] > 0:
                w[l] -= 1
                w[r] -= 1
                count += 1
        if l * 2 > limit:
            count += w[l]
        else:
            count += ((w[l] + 1) // 2)
        return count
        