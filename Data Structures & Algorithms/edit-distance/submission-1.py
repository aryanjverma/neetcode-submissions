class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = {}
        def helper(word1, word2):
            if (word1, word2) in cache:
                return cache[(word1, word2)]
            for i in range(min(len(word1), len(word2))):
                if word1[i] != word2[i]:
                    insert = helper(word1[i:], word1[i] + word2[i:])
                    delete = helper(word1[i:], word2[i + 1:])
                    replace = helper(word1[i:], word1[i] + word2[i + 1:])
                    cache[(word1, word2)] = 1 + min(min(insert, delete), replace)
                    return cache[(word1, word2)]
            cache[(word1, word2)] = abs(len(word1) - len(word2))
            return abs(len(word1) - len(word2))
        answer = helper(word1, word2)
        
        return answer