class Solution:
    def decodeString(self, s: str) -> str:
        string_stack = []
        count_stack = []
        cur = ""
        k = 0
        for c in s:
            if c.isdigit():
                k = k * 10 + int(c)
            elif c == "[":
                string_stack.append(cur)
                count_stack.append(k)
                cur = ""
                k = 0
            elif c == "]":
                cur = string_stack.pop() + cur * count_stack.pop()
            else:
                cur += c
        return cur