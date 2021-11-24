class Portfolio:
    def __init__(self):
        self.holdings = {}  # Key = ticker, Value = number of shares

    def buy(self, ticker, shares):
        self.holdings[ticker] = self.holdings.get(ticker, 0) + shares

    def sell(self, ticker, shares):
        self.holdings[ticker] = self.holdings.get(ticker, 0) - shares

    def __iter__(self):
        return iter(self.holdings.items())


p = Portfolio()
p.buy('ALPHA', 15)
p.buy('BETA', 23)
p.buy('GAMMA', 9)
p.buy('GAMMA', 20)

for (ticker, shares) in p:
    print(ticker, shares)
