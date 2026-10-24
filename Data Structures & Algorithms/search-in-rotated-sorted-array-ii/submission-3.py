class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        right = len(nums) - 1
        while left < right:
            print(left, right)
            mid = (left + right) // 2
            l = nums[left]
            m = nums[mid]
            r = nums[right]
            if l == target or r == target or m == target:
                return True
            if l < target and target < m:
                left += 1
                right = mid - 1
            elif m < target and target < r:
                left = mid + 1
                right -= 1
            elif l < m:
                left = mid + 1
            elif m < r:
                right = mid - 1
            else:
                left += 1
                right -= 1
        return nums[left] == target