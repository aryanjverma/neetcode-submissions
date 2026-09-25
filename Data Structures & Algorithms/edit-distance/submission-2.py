class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = {}
        def helper(index1, index2):
            if index1 == len(word1):
                return len(word2) - index2
            if index2 == len(word2):
                return len(word1) - index1            
            if (index1, index2) in cache:
                return cache[(index1, index2)]
            if word1[index1] == word2[index2]:
                cache[(index1, index2)] = helper(index1 + 1, index2 + 1)
                return cache[(index1, index2)]
            answer = min(helper(index1 + 1, index2), helper(index1, index2 + 1))
            answer = min(answer, helper(index1 + 1, index2 + 1))
            cache[index1, index2] = answer + 1
            return cache[index1, index2]
        
        
        return helper(0, 0)