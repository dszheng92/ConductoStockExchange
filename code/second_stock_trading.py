class StockTrader(object):

    def stock_exchange(self, prices) -> int:
        if len(prices) == 0 or len(prices) == 1:
            return 0

        left_profit = [0 for _ in range(len(prices))]
        right_profit = [0 for _ in range(len(prices))]

        min_prices = prices[0]
        for i in range(1, len(prices)):
            min_prices = min(min_prices, prices[i])
            left_profit[i] = max(left_profit[i - 1], prices[i] - min_prices)

        max_prices = prices[len(prices) - 1]
        for i in range(len(prices) - 2, -1, -1):
            max_prices = max(max_prices, prices[i])
            right_profit[i] = max(right_profit[i + 1], max_prices - prices[i])

        ans = 0
        for i in range(len(prices)):
            if left_profit[i] + right_profit[i] > ans:
                ans = left_profit[i] + right_profit[i]

        return ans

    def run2(self):
        print(self.stock_exchange([2, 4, 6, 1, 3, 8, 3]))
        return self.stock_exchange([2, 4, 6, 1, 3, 8, 3])


if __name__ == '__main__':
    trader = StockTrader()
    trader.run2()
