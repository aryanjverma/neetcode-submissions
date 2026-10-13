class StockSpanner:

    def __init__(self):
        self.con = []

    def next(self, price: int) -> int:
        self.con.append(price)
        i = 0
        while i < len(self.con) and price >= self.con[len(self.con) - 1 - i]:
            i += 1
        return i


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)