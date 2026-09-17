class Solution:
    def canJump(self, nums: List[int]) -> bool:
        index = len(nums) - 1
        for i in range(len(nums) - 2, - 1, - 1):
            if index - i <= nums[i]:
                index = i
        print(index)
        return index == 0