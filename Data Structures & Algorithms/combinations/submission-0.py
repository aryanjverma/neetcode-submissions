class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []
        def helper(array, start):
            if len(array) == k:
                answer.append(array)
            for i in range(start, n + 1):
                helper(array + [i], i + 1)
        helper([], 1)
        return answer