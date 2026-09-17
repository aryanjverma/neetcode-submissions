class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        answer = nums[0]
        currSum = answer
        for i in range(1, len(nums)):
            currSum = max(currSum + nums[i], nums[i])
            answer = max(answer, currSum)
        return answer
