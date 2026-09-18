class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndices = dict()
        for i in range(len(s)):
            lastIndices[s[i]] = i
        i = 0
        answer = []
        while i < len(s):
            ending = lastIndices[s[i]]
            count = 0
            while i <= ending:
                ending = max(lastIndices[s[i]], ending)
                i += 1
                count += 1
            answer.append(count)
        return answer