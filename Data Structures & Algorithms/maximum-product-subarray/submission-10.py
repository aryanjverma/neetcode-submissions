class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        neg = [0] * len(nums)
        pos = [0] * len(nums)
        
        if nums[0] != 0:
            neg[0] = nums[0]
            
        if nums[0] > 0:
            pos[0] = nums[0]
        answer = nums[0]
        for i in range(1, len(nums)):
            neg[i] = nums[i]
            if neg[i - 1] != 0:
                neg[i] *= neg[i - 1]
            answer = max(answer, neg[i])
            pos[i] = nums[i]
            if neg[i - 1] > 0:
                pos[i] = nums[i] * pos[i - 1]
            answer = max(answer, pos[i])
        neg = [0] * len(nums)
        neg[-1] = nums[-1]
        for i in range(len(nums) - 2, - 1, - 1):
            neg[i] = nums[i]
            if neg[i + 1] != 0:
                neg[i] *= neg[i + 1]
            answer = max(answer, neg[i])
        return answer
