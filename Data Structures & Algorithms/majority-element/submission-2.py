class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        answer = 0
        for n in nums:
            if count == 0:
                answer = n
            if answer == n:
                count += 1
            else:
                count -= 1
        return answer
