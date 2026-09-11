import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        answer = [0] * (len(nums) - k + 1)
        q = []
        
        for i in range(k):
            heapq.heappush(q, (-1 * nums[i], i))

        for i in range(len(nums) - k + 1):
            
            heapq.heappush(q, (-1 * nums[i + k - 1], i + k - 1))

            _, index = heapq.heappop(q)
            while index < i or index >= i + k:
                _, index = heapq.heappop(q)
            
            answer[i] = nums[index]
            heapq.heappush(q, (-1 * nums[index], index))
        return answer