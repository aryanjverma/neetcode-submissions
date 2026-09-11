class Solution:
    def minWindow(self, s: str, t: str) -> str:
        charFreqs = defaultdict(int)
        
        for char in t:
            charFreqs[char] += 1
        
        bestLeft = None
        bestRight = None
        
        left = 0
        right = None
        formed = 0
        uniqueLetters = len(charFreqs.keys())
        while left < len(s):
            
            if s[left] in charFreqs:
                if right is None:
                    right = left
                while formed != uniqueLetters:
                    
                    if right >= len(s):
                        if bestLeft is None:
                            return ""
                        return s[bestLeft: bestRight]
                    
                    if s[right] in charFreqs:
                        charFreqs[s[right]] -= 1

                        if charFreqs[s[right]] == 0:
                            formed += 1
                    right += 1
                while s[left] not in charFreqs or charFreqs[s[left]] < 0:
                    if s[left] in charFreqs:
                        charFreqs[s[left]] += 1
                    left += 1
                print(left, right)
                if not bestRight or right - left  < bestRight - bestLeft:
                    bestRight = right
                    bestLeft = left
                charFreqs[s[left]] += 1
                left += 1
                formed -= 1
                while left < len(s) and (s[left] not in charFreqs or charFreqs[s[left]] < 0):
                    if s[left] in charFreqs:
                        charFreqs[s[left]] += 1
                    left += 1
                    
            else:
                left += 1
        if bestLeft is None:
            return ""
        return s[bestLeft: bestRight]