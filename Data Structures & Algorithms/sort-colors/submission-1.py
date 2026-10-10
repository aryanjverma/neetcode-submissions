class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums) - 1
        while left < right:
            while nums[left] == 0:
                left += 1
                if left > right:
                    return
            while nums[right] == 2:
                right -= 1
                if left > right:
                    return
            if nums[left] == 2:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            elif nums[right] == 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            else:
                wasMatch = False
                for i in range(left + 1, right):
                    if nums[i] == 0:
                        nums[left], nums[i] = nums[i], nums[left]
                        left += 1
                        wasMatch = True
                        break
                    elif nums[i] == 2:
                        nums[right], nums[i] = nums[i], nums[right]
                        right -= 1
                        wasMatch = True
                        break
                if not wasMatch:
                    return
                