from collections import deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        prices = [float('inf')] * n
        prices[src] = 0
        for i in range(k + 1):
            newPrices = prices.copy()
            for flight in flights:
                a, b, c = flight
                newPrices[b] = min(newPrices[b], prices[a] + c)
            prices = newPrices
        if prices[dst] == float('inf'):
            return -1
        return prices[dst]