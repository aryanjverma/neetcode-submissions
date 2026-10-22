class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 1
        s = nums[left]
        answer = float('inf')
        while right <= len(nums):
            while right < len(nums) and s < target:
                s += nums[right]
                right += 1
            if s < target:
                break
            while left < right and s - nums[left] >= target:
                s -= nums[left]
                left += 1
            
            answer = min(answer, right - left)
            s -= nums[left]
            left += 1
        if answer == float('inf'):
            return 0
        return answer