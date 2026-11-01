class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.answer = 0
        
        def helper(i, currXor):
            if i >= len(nums):
                self.answer += currXor
                return
            helper(i + 1, currXor)
            helper(i + 1, currXor ^ nums[i])
        helper(0, 0)
        return self.answer