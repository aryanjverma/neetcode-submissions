class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        sums = [0] * (len(nums) + 1)
        sums[1] = nums[0]
        for i in range(2, len(nums) + 1):
            sums[i] = sums[i - 1] + nums[i - 1]
        dp = {}
        def helper(index, remaining):
            if (index, remaining) in dp:
                return dp[(index, remaining)]
            if remaining == 1:
                return sums[len(nums)] - sums[index]
            minSum = float('inf')
            for i in range(index + 1, len(nums) - remaining + 2):
                front = sums[i] - sums[index]
                back = helper(i, remaining - 1)
                
                minSum = min(minSum, max(front, back))
            dp[(index, remaining)] = minSum
            return minSum
        answer = helper(0, k)
        
        return answer