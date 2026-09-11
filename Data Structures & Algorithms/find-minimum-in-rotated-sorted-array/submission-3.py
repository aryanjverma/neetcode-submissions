class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2
        while (left < mid and mid < right):
            if nums[left] < nums[mid] and nums[mid] < nums[right]:
                return nums[left]
            if nums[left] < nums[mid]:
                left = mid
            elif nums[mid] < nums[right]:
                right = mid
            mid = (left + right) // 2
            
        return min(nums[left], min(nums[mid], nums[right]))
