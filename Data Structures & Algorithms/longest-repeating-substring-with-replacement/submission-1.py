class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        maxLength = 0
        charCounts = defaultdict(int)
        
        while right < len(s):
            charCounts[s[right]] += 1
            while right - left + 1 - max(charCounts.values()) > k:
                charCounts[s[left]] -= 1
                left += 1
            maxLength = max(right - left + 1, maxLength)
            right += 1

        return maxLength