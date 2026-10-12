class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n < 3:
            return 1
        t1 = 0
        t2 = 1
        t3 = 1
        for i in range(n - 2):
            print(t1, t2, t3)
            temp = t2
            t3 += (t2 + t1)
            t2 = t3 - (t1 + t2)
            t1 = temp
        return t3