class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        def helper(string, rLeft, rRight, check):
            
            if check >= 0:
                if rLeft == 0 and rRight == 0:
                    answer.append(string)
                elif rLeft >= 0 and rRight >= 0:
                    helper(string + "(", rLeft - 1, rRight, check + 1)
                    helper(string + ")", rLeft, rRight - 1, check - 1)
        helper("", n, n, 0)
        return answer