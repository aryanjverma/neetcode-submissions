class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        highestLeft = [height[0]] * len(height)
        highestRight = [height[-1]] * len(height)
        for i in range(1, len(height)):
            highestLeft[i] = max(highestLeft[i - 1], height[i - 1])
            index = len(height) - i - 1
            highestRight[index] = max(highestRight[index + 1], height[index + 1])
        
        water = 0
        for i in range(1, len(height) - 1):
            water += max(0, min(highestLeft[i], highestRight[i]) - height[i])
            
        return water