class Solution:
    def reverseBits(self, n: int) -> int:
        answer = 0
        for i in range(16):
            temp1 = (n >> i) % 2
            temp2 = (n >> (31 - i)) % 2
            print(temp1, temp2)
            answer += (temp2 << i)
            answer += (temp1 << (31 - i))
        return answer