class Solution:
    def longestPalindrome(self, s: str) -> str:
        bestLeft = 0
        bestRight = 1
        left = 0
        while left < len(s):
            
            right = left + 1
            while right < len(s) and s[left] == s[right]:
                right += 1
            temp = right
            while left > 0 and right < len(s) and s[left - 1] == s[right]:
                left -= 1
                right += 1
            if right - left > bestRight - bestLeft:
                bestRight = right
                bestLeft = left
            left = temp
        return s[bestLeft: bestRight]