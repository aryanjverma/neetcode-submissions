class Solution:
    def partition(self, s: str) -> List[List[str]]:
        answer = []
        def isPalindrome(front, back):
            while front < back:
                if s[front] != s[back]:
                    return False
                front += 1
                back -= 1
            return True
        def helper(currAnswer):
            starting = 0
            if len(currAnswer) > 0:
                starting = currAnswer[-1]
                if starting == len(s):
                    prev = 0
                    result = []
                    for index in currAnswer:
                        result.append(s[prev: index])
                        prev = index
                    answer.append(result)
                    return
            for i in range(starting, len(s)):
                if isPalindrome(starting, i):
                    helper(currAnswer + [i + 1])
        helper([])
        return answer