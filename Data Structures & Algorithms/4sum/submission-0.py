class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        answers = set()
        for i in range(len(nums) - 3):
            num1 = nums[i]
            for j in range(i + 1, len(nums) - 2):
                newTarget = target - (num1 + nums[j])
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    newSum = nums[left] + nums[right]
                    if newSum == newTarget:
                        answers.add((num1, nums[j], nums[left], nums[right]))
                        left += 1
                        right -= 1
                    elif newSum > newTarget:
                        right -= 1
                    else:
                        left += 1
        result = []
        for answer in answers:
            result.append([answer[0], answer[1], answer[2], answer[3]])
        return result