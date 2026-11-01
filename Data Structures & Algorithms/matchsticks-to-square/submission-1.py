class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        length = sum(matchsticks)
        if length % 4 != 0:
            return False
        length //= 4
        sides = [length] * 4
        for stick in matchsticks:
            if stick > length:
                return False
        def helper(index):
            if index >= len(matchsticks):
                for side in sides:
                    if side != 0:
                        return False
                return True
            stick = matchsticks[index]
            for i in range(4):
                if stick <= sides[i]:
                    sides[i] -= stick
                    if helper(index + 1):
                        sides[i] += stick
                        return True
                    sides[i] += stick
            return False
        return helper(0)