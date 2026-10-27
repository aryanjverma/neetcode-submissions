import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        d = defaultdict(int)
        for char in s:
            d[char] += 1
        q = []
        for char in d:
            heapq.heappush(q, (- d[char], char))
        answer = ""
        while q:
            freq, char = heapq.heappop(q)
            if len(answer) > 0 and answer[-1] == char:
                if len(q) > 0:
                    tempFreq, tempChar = freq, char
                    freq, char = heapq.heappop(q)
                    heapq.heappush(q, (tempFreq, tempChar))
                else:
                    return ""
            answer += char
            if freq < - 1:
                heapq.heappush(q, (freq + 1, char))
        return answer