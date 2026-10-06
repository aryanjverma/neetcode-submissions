class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        dp = {}
        def helper(left, right):
            if left > right:
                return 0
            if (left, right) in dp:
                return dp[(left, right)]
            answer = 0
            leftBal = 1 if left <= 0 else nums[left - 1]
            rightBal = 1 if right >= (len(nums) - 1) else nums[right + 1]
            for i in range(left, right + 1):
                newAnswer = nums[i] * leftBal * rightBal
                newAnswer += helper(left, i - 1)
                newAnswer += helper(i + 1, right)
                answer = max(answer, newAnswer)
            dp[(left, right)] = answer
            return answer
        answer = helper(0, len(nums) - 1)
        
        return answer
        
