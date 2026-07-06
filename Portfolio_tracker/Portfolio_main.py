stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 130
}

total_investment = 0

print("=== Stock Portfolio Tracker ===")
print("Available Stocks:", ", ".join(stock_prices.keys()))

number_of_stocks = int(input("\nEnter the number of stocks you want to add: "))

for i in range(number_of_stocks):
    print(f"\nStock {i + 1}")

    stock_name = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    if stock_name in stock_prices:
        investment = stock_prices[stock_name] * quantity
        total_investment += investment

        print(f"Investment in {stock_name}: ${investment}")

    else:
        print("Stock not available.")

print("\n=== Portfolio Summary ===")
print(f"Total Investment Value: ${total_investment}")