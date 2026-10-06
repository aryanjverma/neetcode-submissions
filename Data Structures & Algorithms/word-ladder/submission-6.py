from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        stringLength = len(endWord)
        visited = set()
        q = deque()
        q.append((beginWord, 0))
        while q:
            beginWord, d = q.popleft()
            print(beginWord)
            visited.add(beginWord)
            if beginWord == endWord:
                return d + 1
            for i in range(stringLength):
                for word in wordList:
                    if word not in visited:
                        diff = 0
                        if beginWord[i] != word[i] and beginWord[:i] == word[:i] and beginWord[i + 1:] == word[i + 1:]:
                            q.append((word, d + 1))
        return 0