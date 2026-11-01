import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        q = []
        if a != 0:
            heapq.heappush(q, (- a, "a"))
        if b != 0:
            heapq.heappush(q, (- b, "b"))
        if c != 0:
            heapq.heappush(q, (- c, "c"))
        answer = []
        while q:
            
            freq, letter = heapq.heappop(q)
            if freq == 0:
                continue
            
            if len(answer) < 2 or (answer[- 1] != letter or answer[- 2] != letter):
                answer.append(letter)
                if freq + 1 != 0:
                    heapq.heappush(q, (freq + 1, letter))
            elif len(q) > 0 and q[0][0] != 0:
                newFreq, newLetter = heapq.heappop(q)
                answer.append(newLetter)
                answer.append(letter)
                heapq.heappush(q, (newFreq + 1, newLetter))
                heapq.heappush(q, (freq + 1, letter))
        return "".join(answer)