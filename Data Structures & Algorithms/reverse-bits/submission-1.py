class Solution:
    def reverseBits(self, n: int) -> int:
        answer = 0
        for i in range(16):
            answer += (((n >> i) % 2) << (31 - i))
            answer += (((n >> (31 - i)) % 2) << i)
        return answer