class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        d = dict()
        for word in dictionary:
            d[word] = 0
        
        def helper(left, right):
            split = s[left: right]
            if split in d:
                return d[split]
            answer = right - left
            for i in range(left + 1, right):
                answer = min(answer, helper(left, i) + helper(i, right))
            d[split] = answer
            return answer
        return helper(0, len(s))