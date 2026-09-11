class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(left, right, target, nums):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1
        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2
        
        while left <= mid and mid <= right:
            leftNum = nums[left]
            if target == leftNum:
                return left
            midNum = nums[mid]
            if target == midNum:
                return mid
            rightNum = nums[right]
            if target == rightNum:
                return right
            if leftNum > target and rightNum < target:
                return - 1
            if leftNum <= midNum:
                if leftNum <= target <= midNum:
                    return binarySearch(left + 1, mid - 1, target, nums)
                else:
                    left = mid + 1 
            elif midNum <= rightNum:
                if midNum <= target <= rightNum:
                    return binarySearch(mid + 1, right - 1, target, nums)
                else:
                    right = mid - 1
            mid = (left + right) // 2    
                 
        return -1
            