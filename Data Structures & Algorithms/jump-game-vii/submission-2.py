from collections import deque
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        end = len(s) - 1
        q = deque()
        q.append(0)
        visited = set()
        while q:
            currPos = q.popleft()
            if currPos not in visited:
                visited.add(currPos)
                if currPos == end:
                    return True
                for i in range(min(end, maxJump + currPos), currPos + minJump - 1, - 1):         
                    if s[i] == '0':
                        q.append(i)
        return False