class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}

        def helper(index):
            if index == len(s):
                return True
            if index in dp:
                return dp[index]
            for word in wordDict:
                isMatch = True
                if index + len(word) - 1 < len(s):
                    for i in range(len(word)):
                        if word[i] != s[index + i]:
                            isMatch = False
                            break
                    if isMatch and helper(index + len(word)):
                        return True
            dp[index] = False
            return False
        
        return helper(0)