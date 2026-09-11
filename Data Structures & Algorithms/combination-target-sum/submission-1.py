class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer = []
        def helper(i, currDiff, currArray):
            if currDiff == 0:
                answer.append(currArray)
            if currDiff > 0:
                for i in range(i, len(nums)):
                    helper(i, currDiff - nums[i], currArray + [nums[i]])
        helper(0, target, [])
        return answer