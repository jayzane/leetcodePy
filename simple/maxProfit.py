class Solution:
    def maxProfit(self, prices):
        profit = 0
        buy_index = 0
        sell_index = buy_index + 1
        while buy_index < len(prices):
            tmp_profit = 0
            while sell_index < len(prices) and prices[sell_index] > prices[sell_index - 1]:
                tmp_profit = prices[sell_index] - prices[buy_index]
                sell_index += 1
            if tmp_profit > 0:
                profit += tmp_profit
                print('buy day:%s sell day: %s profit: %s' % (buy_index, sell_index, tmp_profit))
                buy_index = sell_index
            else:
                buy_index += 1
            sell_index = buy_index + 1
        return profit


if __name__ == '__main__':
    sol = Solution()
    array = [7,1,5,3,6,4]
    print(sol.maxProfit(array))
