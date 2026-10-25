class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(max_sum):
            subarray_count = 1
            current_sum = 0 
            
            for num in nums:
                current_sum += num
                if current_sum > max_sum:
                    subarray_count += 1
                    current_sum = num
            return subarray_count <= k
        left = max(nums)
        right = sum(nums)
        answer = right
        while left <= right:
            mid = (left + right) // 2
            if canSplit(mid):
                answer = mid
                right = mid - 1
            else:
                left = mid + 1
        return answer
