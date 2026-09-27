import ctypes

class Solution:
    def getSum(self, a: int, b: int) -> int:
        bitMask = 0xFFFFFFFF
        answer = 0
        c = 0
        for i in range(32):

            la = (a >> i) & (1)
            lb = (b >> i) & (1)
            x = la ^ lb ^ c
            c = la & lb | la & c | lb & c
            answer |= (x << i)
        
        return ctypes.c_int32(answer).value