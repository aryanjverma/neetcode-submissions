class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        for i in range(len(nums) - k - 1, - 1, - 1):
            for j in range(i, i + k):
                nums[j], nums[j + 1] = nums[j + 1], nums[j]