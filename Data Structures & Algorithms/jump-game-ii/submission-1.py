class Solution:
    def jump(self, nums: List[int]) -> int:
        nums[-1] = 0
        for i in range(len(nums) - 2, - 1, - 1):
            nums[i] = 1 + min(nums[i + 1], nums[min(len(nums) - 1, nums[i] + i)])
        
        return nums[0]