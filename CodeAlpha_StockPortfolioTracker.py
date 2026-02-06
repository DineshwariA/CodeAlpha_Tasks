# Stock Portfolio Tracker

stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 320
}

print("Available Stocks:")
for stock in stocks:
    print(stock, "-> Price:", stocks[stock])

stock_name = input("\nEnter stock name: ").upper()

if stock_name in stocks:
    quantity = int(input("Enter quantity: "))

    total_value = stocks[stock_name] * quantity

    print("\nStock:", stock_name)
    print("Price per stock:", stocks[stock_name])
    print("Quantity:", quantity)
    print("Total Investment Value:", total_value)

else:
    print("Invalid stock name!")



