class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        answer = nums[0]
        result = nums[0]
        for i in range(1, len(nums)):
            if result == 0:
                result = nums[i]
            else:
                result = nums[i] * result
            answer = max(answer, result)
        result = nums[-1]
        answer = max(answer, nums[-1])
        for i in range(len(nums) - 2, - 1, - 1):
            if nums[i] == 0:
                result = nums[i]
            else:
                result = nums[i] * result
            answer = max(answer, result)
        return answer