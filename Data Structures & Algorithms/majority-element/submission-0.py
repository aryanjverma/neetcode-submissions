class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        num = nums[0]
        for i in range(1, len(nums)):
            if num == nums[i]:
                count += 1
            else:
                count -= 1
                if count == -1:
                    num = nums[i]
                    count = 1
        return num
