class StockSpanner:

    def __init__(self):
        self.con = []

    def next(self, price: int) -> int:
        
        i = 1
        while self.con and price >= self.con[-1][0]:
            i += self.con[-1][1]
            self.con.pop()
        self.con.append((price, i))
        return i


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)