class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        freq = defaultdict(int)

        for i in range(len(s1)):
            freq[s1[i]] -= 1
            freq[s2[i]] += 1
        
        left = 0
        right = len(s1) - 1

        while right < len(s2):
            isPerm = True
            for value in freq.values():
                if value != 0:
                    isPerm = False
                    break
            if isPerm:
                return True
            freq[s2[left]] -= 1
            left += 1
            right += 1
            if right < len(s2):
                freq[s2[right]] += 1
        return False