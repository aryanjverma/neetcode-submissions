from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        visited = set()
        q = deque()
        q.append((beginWord, 0))
        while q:
            beginWord, d = q.popleft()
            visited.add(beginWord)
            if beginWord == endWord:
                return d + 1
            for word in wordList:
                if word not in visited:
                    diff = 0
                    for i in range(len(word)):
                        if beginWord[i] != word[i]:
                            diff += 1  
                    if diff == 1:
                        q.append((word, d + 1))
        return 0