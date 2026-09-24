class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def helper(index, target):
            if index == len(nums):
                return 1 if target == 0 else 0
            if (index, target) in dp:
                return dp[(index, target)]
            answer = helper(index + 1, target + nums[index]) + helper(index + 1, target - nums[index])
            dp[(index, target)] = answer
            return answer
        answer = helper(0, target)
        
        return answer