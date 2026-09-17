class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        maxAnswer = 1
        for i in range(1, len(nums)):
            answer = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    answer = max(answer, 1 +dp[j])
            dp[i] = answer
            maxAnswer = max(maxAnswer, answer)
        return maxAnswer