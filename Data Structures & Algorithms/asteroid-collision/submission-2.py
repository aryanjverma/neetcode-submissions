class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            if len(stack) == 0:
                stack.append(asteroid)
            elif stack[-1] > 0 and asteroid < 0:
                
                foundMatch = False
                
                while len(stack) > 0 and stack[-1] > 0 and stack[-1] < abs(asteroid):
                    stack.pop()
                
                if len(stack) == 0:
                    stack.append(asteroid)
                elif stack[-1] > 0 and asteroid < 0 and stack[-1] == abs(asteroid):
                    stack.pop()
                elif stack[-1] * asteroid > 0:
                    stack.append(asteroid)
            else:
                stack.append(asteroid)
        return stack
            