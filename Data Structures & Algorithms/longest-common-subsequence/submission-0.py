class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        saved = {}
        def helper(index1, index2):
            if index1 >= len(text1) or index2 >= len(text2):
                return 0
            if (index1, index2) in saved:
                return saved[(index1, index2)]
            if text1[index1] == text2[index2]:
                answer = 1 + helper(index1 + 1, index2 + 1)
            else:
                answer = max(helper(index1 + 1, index2), helper(index1, index2 + 1))
            saved[(index1, index2)] = answer
            return answer
        return helper(0, 0)