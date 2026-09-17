class Solution:
    def isHappy(self, n: int) -> bool:
        viewed = set()
        while n != 1 and n not in viewed:
            viewed.add(n)
            number = 0
            while n > 0:
                number += ((n % 10) * (n % 10))
                n //= 10
            
            n = number
        
        return n == 1