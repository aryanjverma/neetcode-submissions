class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)

        for i in range(len(temperatures) - 2, - 1, - 1):
            j = i + 1
            while temperatures[j] <= temperatures[i]:
                if answer[j] == 0:
                    j = i
                    break
                j += answer[j]
            answer[i] = j - i
        return answer