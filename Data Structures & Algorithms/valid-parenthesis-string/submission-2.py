class Solution:
    def checkValidString(self, s: str) -> bool:
        
        leftStack = []
        starStack = []
        for i in range(len(s)):
            char = s[i]
            if char == "(":
                leftStack.append(i)
            elif char == "*":
                starStack.append(i)
            else:
                if leftStack:
                    leftStack.pop()
                elif starStack:
                    starStack.pop()
                else:
                    return False
        while leftStack and starStack:
            left = leftStack.pop()
            flag = False
            while starStack and left > starStack.pop():
                pass
            
        return len(leftStack) == 0