import math
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 1:
            return 1
        if x == -1:
            if n % 2 == 0:
                return 1
            else:
                return - 1
        if n == 0:
            return 1
        isNeg = False
        if n < 0:
            isNeg = True
            n *= -1
        new = int(math.log(n, 2))
        n -= (1 << new)
        answer = x
        while new > 0:
            answer *= answer
            new -= 1
        while n > 0:
            answer *= x
            n -= 1
        if isNeg:
            return 1 / answer
        return answer