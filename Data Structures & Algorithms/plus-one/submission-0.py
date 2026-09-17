class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        index = len(digits) - 1
        while carry == 1 and index >= 0:
            number = digits[index] + carry
            digits[index] = number % 10
            carry = number // 10
            index -= 1
        if carry == 1:
            digits.insert(0, carry)
        return digits