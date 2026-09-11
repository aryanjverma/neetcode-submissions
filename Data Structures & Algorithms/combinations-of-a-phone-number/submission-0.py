class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        digitMap = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        answer = []
        def helper(digits, currAnswer): 
            if len(digits) == 0:
                answer.append(currAnswer)
            else:
                letters = digitMap[digits[0]]
                for letter in letters:
                    helper(digits[1:], currAnswer + letter)
        helper(digits, "")
        return answer
