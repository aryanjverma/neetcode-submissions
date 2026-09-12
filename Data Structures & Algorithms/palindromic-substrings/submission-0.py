class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        left = 0
        while left < len(s):
            right = left + 1
            tempCount = 1
            while right < len(s) and s[left] == s[right]:
                tempCount += 1        
                right += 1
            tempCount = (tempCount * (tempCount + 1)) // 2
            count += tempCount
            temp = right
            while left > 0 and right < len(s) and s[left - 1] == s[right]:
                count += 1
                left -= 1
                right += 1
            left = temp
        return count