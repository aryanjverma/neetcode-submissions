class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        answer = 1
        while answer in nums and answer <= len(nums):
            answer += 1
        return answer