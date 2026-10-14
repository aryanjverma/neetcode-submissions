class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total_sum = sum(stones)
        target = total_sum // 2
        dp = {}
        def helper(i, curr_sum):
            if curr_sum == target:
                return curr_sum
            if i == len(stones) or curr_sum > target:
                return curr_sum
            if (i, curr_sum) in dp:
                return dp[(i, curr_sum)]
            
            a1 = helper(i + 1, curr_sum)
            a2 = helper(i + 1, curr_sum + stones[i])
            if abs(a1 - target) < abs(a2 - target):
                dp[(i, curr_sum)] = a1
            else:
                dp[(i, curr_sum)] = a2
            
            return dp[(i, curr_sum)]
        return abs(total_sum - 2 * helper(0, 0))