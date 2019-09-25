from test_framework import generic_test


def buy_and_sell_stock_once(prices):
    max_profit = 0.
    low_price = prices[0]
    n_days = len(prices)
    for i in range(1, n_days):
        p = prices[i]
        if p - low_price > max_profit:
            max_profit = p - low_price
        if low_price > p:
            low_price = p
    return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
