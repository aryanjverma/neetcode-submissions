class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustCount = [0] * (n + 1)
        trusters = set()
        for t in trust:
            a, b = t
            trusters.add(a)
            trustCount[b] += 1
        judge = -1
        for i in range(1, n + 1):
            if i not in trusters and trustCount[i] == n - 1:
                if judge == -1:
                    judge = i
                else:
                    return - 1
        return judge