class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        if num1 =="1":
            return num2
        if num2 =="1":
            return num1
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        carry = 0
        answer = ""
        num1 = "".join(reversed(num1))
        num2 = "".join(reversed(num2))
        for i in range(len(num1)):
            result = carry
            for j in range(min(i + 1, len(num2))):
                char1 = num1[i - j]
                char2 = num2[j]
                n1 = ord(char1) - 48
                n2 = ord(char2) - 48
                result += (n1 * n2)
            answer += str(result % 10)
            carry = (result // 10)
        for j in range(1, len(num2)):
            result = carry
            for i in range(j, len(num2)):
                char1 = num1[len(num1) - 1 - (i - j)]
                char2 = num2[i]
                n1 = ord(char1) - 48
                n2 = ord(char2) - 48
                result += (n1 * n2)
            answer += str(result % 10)
            carry = (result // 10)
        if carry != 0:
            answer += str(carry)
        return answer[::-1]