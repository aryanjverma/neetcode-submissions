class Solution:
    def reverse(self, x: int) -> int:
        neg = 1
        if x < 0:
            neg = -1
            x *= - 1
        
        answer = 0
        while x > 0:
            answer = answer * 10
            answer += (x % 10)
            x //= 10
            if answer > (2 << 31 - 1):
                return 0    
        return answer * neg