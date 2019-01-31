# -*- coding: utf-8 -*-

class StockSpanner(object):

    def __init__(self):
        self.prices = []
        self.spans = []

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        span = 1
        r = len(self.prices) - 1
        while r >= 0 and price >= self.prices[r]:
            span += self.spans[r]
            r -= self.spans[r]
        self.prices.append(price)
        self.spans.append(span)
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

if __name__ == '__main__':
    ops = ["StockSpanner","next","next","next","next","next","next","next"]
    args = [[],[100],[80],[60],[70],[60],[75],[85]]

    obj = locals()[ops[0]](*args[0])

    for i in xrange(1, len(ops)):
        print getattr(obj, ops[i])(*args[i])
