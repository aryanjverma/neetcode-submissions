class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        left = 0
        right = 0
        currChars = set()
        maxLength = 0
        for char in s:
            if char in currChars:
                maxLength = max(maxLength, right - left)
                while s[left] != char:
                    currChars.remove(s[left])
                    left += 1
                currChars.add(char)
                left += 1
            else:
                currChars.add(char)
            right += 1
        return max(right - left, maxLength)