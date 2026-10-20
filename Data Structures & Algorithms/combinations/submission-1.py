class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []
        def helper(array, start):
            if len(array) == k:
                answer.append(array.copy())
            for i in range(start, n + 1):
                array.append(i)
                helper(array, i + 1)
                array.pop()
        helper([], 1)
        return answer