class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        self.answer = 0
        self.canBuy = True
        visited = set()
        def helper(index, currSum):
            if (index, currSum, self.canBuy) not in visited:
                self.answer = max(self.answer, currSum)
                if index < len(prices):
                    visited.add((index, currSum, self.canBuy))
                    if self.canBuy:
                        self.canBuy = False
                        helper(index + 1, currSum - prices[index])
                        self.canBuy = True
                        helper(index + 1, currSum)

                    else:
                        self.canBuy = True
                        helper(index + 2, currSum + prices[index])
                        self.canBuy = False
                        helper(index + 1, currSum)
        
        helper(0, 0)
        
        return self.answer