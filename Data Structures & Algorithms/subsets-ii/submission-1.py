class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        answer = []

        nums.sort()
        def helper(currAnswer, currIndex):
            print(currAnswer, currIndex)
            if currIndex <= len(nums):
                answer.append(currAnswer)
                maxNumber = -21
                for i in range(currIndex, len(nums)):
                    if nums[i] > maxNumber:
                        helper(currAnswer + [nums[i]], i + 1)
                        maxNumber = nums[i]
        helper([], 0);
        return answer

        