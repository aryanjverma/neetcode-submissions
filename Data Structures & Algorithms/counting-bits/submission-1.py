class Solution:
    def countBits(self, n: int) -> List[int]:
        counts = [0] * (n + 1)
        
        for i in range(1, n + 1):
            
            counts[i] = 1 + counts[i - 2 ** math.floor(math.log2(i))]
        return counts