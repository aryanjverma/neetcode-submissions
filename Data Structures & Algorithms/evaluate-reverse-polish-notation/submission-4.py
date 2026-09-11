class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numberStack = []
        result = 0
        for token in tokens:
            if token == "+":
                numberStack.append(numberStack.pop() + numberStack.pop())
            elif token == "*":
                numberStack.append(numberStack.pop() * numberStack.pop())
            elif token == "-":
                second = numberStack.pop()
                first = numberStack.pop()
                numberStack.append(first - second)
            elif token == "/":
                second = numberStack.pop()
                first = numberStack.pop()
                numberStack.append(int(first / second))
            else:
                numberStack.append(int(token))
        return numberStack.pop()
        
