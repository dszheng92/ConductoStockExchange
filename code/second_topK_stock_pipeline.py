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

    def run2(self):
        self.update('Alibaba', 1200)
        self.update('Tencent', 200)
        self.update('Bilibili', 100)
        self.update('Bilibili', 300)
        self.update('Bilibili', 700)
        self.update('JD', 500)
        self.update('Baidu', 300)
        self.update('Baidu', 700)
        self.update('Bytedance', 900)
        self.update('Huobi', 800)
        self.update('Bytedance', 500)
        self.update('Sohu', 50)
        self.update('Bytedance', 150)
        print(self.getTopK())
        return self.getTopK()


if __name__ == '__main__':
    exchange = ElectronicExchange()
    exchange.run2()

