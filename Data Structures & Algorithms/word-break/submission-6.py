from collections import deque
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        results = dict()
        
        def dfs(string):
            if string in results:
                return results[string]
            if string == "":
                return True
            for word in wordDict:
                if len(word) <= len(string):
                    isMatch = True
                    for i in range(len(word)):
                        if string[i] != word[i]:
                            isMatch = False
                            break
                    if isMatch and dfs(string[len(word):]):
                        results[string] = True
                        return True
            results[string] = False
            return False
        print(results)
        return dfs(s)