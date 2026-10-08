class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = strs[0]
        for i in range(1, len(strs)):
            j = 0
            for char in pre:
                if len(strs[i]) <= j or char != strs[i][j]:
                    break
                j += 1
            pre = pre[:j]
        return pre