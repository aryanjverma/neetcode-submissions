class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        dis = right - left
        count = 0
        while dis > 0:
            count += 1
            dis //= 2
        
        mask = (((1 << (32 - count)) - 1) << count)
        
        return left & mask & right