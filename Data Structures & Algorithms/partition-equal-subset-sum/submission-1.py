class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        targetVal = sum(nums)
        if targetVal % 2 == 1:
            return False
        targetVal //= 2
        
        def recurse(index, target):
            if target < 0 or index >= len(nums):
                return False
            if target == 0:
                return True
            for i in range(index, len(nums)):
                if recurse(index + 1, target - nums[index]) or recurse(index + 1, target):
                    return True
            return False
        return recurse(0, targetVal)
