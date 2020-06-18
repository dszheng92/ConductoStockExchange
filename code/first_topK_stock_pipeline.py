import collections
import heapq


class ElectronicExchange:
    def __init__(self):
        self.topK = []
        self.stocks = collections.defaultdict(int)

    def update(self, stock, volume):
        self.stocks[stock] += volume
        for i, pair in enumerate(self.topK):
            _, s = pair
            if stock == s:
                self.topK[i][0] = self.stocks[stock]
                heapq.heapify(self.topK)
                return

        if len(self.topK) < 10:
            heapq.heappush(self.topK, [self.stocks[stock], stock])
        elif self.topK[0][0] < self.stocks[stock]:
            heapq.heappushpop(self.topK, [self.stocks[stock], stock])

    def getTopK(self):
        for a, b in self.topK:
            print(a, b)
        return [s for _, s in self.topK]

    def run1(self):
        self.update('bloomberg', 300)
        self.update('apple', 700)
        self.update('amazon', 900)
        self.update('google', 1100)
        self.update('twitter', 600)
        self.update('bloomberg', 1200)
        self.update('facebook', 200)
        self.update('instacart', 100)
        self.update('bloomberg', 300)
        self.update('macys', 700)
        self.update('oldnavy', 500)
        self.update('warnar', 350)
        self.update('acne', 50)
        self.update('thestandard', 150)
        print(self.getTopK())
        return self.getTopK()


if __name__ == '__main__':
    exchange = ElectronicExchange()
    exchange.run1()
