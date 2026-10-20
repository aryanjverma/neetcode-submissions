from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        q = deque()
        q.append(("0000",0))
        visited = set(deadends)
        visited.add("0000")
        while q:
            code, distance = q.popleft()
            if code == target:
                return distance
            
            for i in range(4):
                targetLetter = int(code[i])
                for move in [1, - 1]:
                    next_digit = (targetLetter + move) % 10
                    newCode = code[:i] + str(next_digit) + code[i + 1:]
                    if newCode not in visited:
                        visited.add(newCode)
                        q.append((newCode, distance + 1))
        return -1