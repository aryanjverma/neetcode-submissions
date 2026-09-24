class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        
        
        visited = dict()
        def helper(index, canBuy):
            if (index, canBuy) in visited:
                return visited[(index, canBuy)]
            if index >= len(prices):
                return 0
            answer = 0
            if canBuy:
                answer = max(answer, helper(index + 1, False) - prices[index])
                answer = max(answer, helper(index + 1, True))
            else:
                answer = max(answer, helper(index + 2, True) + prices[index])
                answer = max(answer, helper(index + 1, False))
            visited[index, canBuy] = answer
            return answer

        return helper(0, True)