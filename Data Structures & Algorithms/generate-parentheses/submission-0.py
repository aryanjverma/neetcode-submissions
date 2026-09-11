class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        def helper(string, rLeft, rRight):
            check = 0
            for char in string:
                if char == ")":
                    check -= 1
                else:
                    check += 1
            if check >= 0:
                if rLeft == 0 and rRight == 0:
                    answer.append(string)
                elif rLeft >= 0 and rRight >= 0:
                    helper(string + "(", rLeft - 1, rRight)
                    helper(string + ")", rLeft, rRight - 1)
        helper("", n, n)
        return answer