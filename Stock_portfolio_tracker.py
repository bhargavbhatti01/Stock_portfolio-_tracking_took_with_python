import requests

API_KEY = 'RXJFOR4CL99XUXCJ'


def get_stock_price(symbol):
    url = f'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    try:
        price = float(data['Global Quote']['05. price'])
        return price
    except KeyError:
        print("Error: Unable to retrieve stock price for symbol", symbol)
        return None

def get_stock_info(symbol):
    url = f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={symbol}&apikey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    try:
        stock_info = data['bestMatches'][0]
        stock_name = stock_info['2. name']
        return stock_name
    except (KeyError, IndexError):
        print("Error: Unable to retrieve stock info for symbol", symbol)
        return None
1

class Portfolio:
    def __init__(self):
        self.stocks = {}

    def add_stock(self, symbol, quantity):
        if symbol in self.stocks:
            self.stocks[symbol] += quantity
        else:
            self.stocks[symbol] = quantity

    def remove_stock(self, symbol, quantity):
        if symbol in self.stocks:
            if self.stocks[symbol] > quantity:
                self.stocks[symbol] -= quantity
            else:
                del self.stocks[symbol]

    def track_performance(self):
        print("Stock Portfolio Performance:")
        print("---------------------------------")
        for symbol, quantity in self.stocks.items():
            price = get_stock_price(symbol)
            stock_name = get_stock_info(symbol)
            if price is not None and stock_name is not None:
                total_investment = price * quantity
                current_value = price * quantity
                profit_loss = current_value - total_investment
                print(f"Name: {stock_name}, Symbol: {symbol}, Quantity: {quantity}, Current Price: {price}, Total Investment: {total_investment}, Current Value: {current_value}, Profit/Loss: {profit_loss}")

    def view_holdings(self):
        print("Current Holdings:")
        print("---------------------------------")
        for symbol, quantity in self.stocks.items():
            print(f"Symbol: {symbol}, Quantity: {quantity}")


def main():
    portfolio = Portfolio()

    while True:
        print("\nStock Portfolio Tracker")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. Track Performance")
        print("4. View Current Holdings")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            symbol = input("Enter stock symbol: ").upper()
            quantity = int(input("Enter quantity: "))
            portfolio.add_stock(symbol, quantity)
            print(f"Stock {symbol} added successfully.")
        elif choice == '2':
            symbol = input("Enter stock symbol: ").upper()
            quantity = int(input("Enter quantity: "))
            portfolio.remove_stock(symbol, quantity)
            print(f"Stock {symbol} removed successfully.")
        elif choice == '3':
            portfolio.track_performance()
        elif choice == '4':
            portfolio.view_holdings()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
