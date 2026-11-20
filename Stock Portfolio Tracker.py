
# Stock Portfolio Tracker

# Dictionary containing stock names and prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190
}

portfolio = {}
total_investment = 0

print("====================================")
print("       STOCK PORTFOLIO TRACKER")
print("====================================")

print("\nAvailable Stocks and Prices:")

for stock, price in stock_prices.items():
    print(stock, ":", "$", price)

# Take input from user
num_stocks = int(input("\nHow many different stocks do you want to buy? "))

for i in range(num_stocks):

    stock_name = input("\nEnter stock name: ").upper()

    if stock_name in stock_prices:

        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero!")
            continue

        investment = stock_prices[stock_name] * quantity

        portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity

        total_investment += investment

        print("Investment in", stock_name, "=", "$", investment)

    else:
        print("Stock not available!")

# Display portfolio summary
print("\n====================================")
print("        PORTFOLIO SUMMARY")
print("====================================")

for stock, quantity in portfolio.items():
    value = stock_prices[stock] * quantity
    print(stock, "| Quantity:", quantity, "| Value: $", value)

print("------------------------------------")
print("Total Investment Value: $", total_investment)

# Save portfolio in a text file
with open("portfolio.txt", "w") as file:

    file.write("STOCK PORTFOLIO SUMMARY\n")
    file.write("=======================\n")

    for stock, quantity in portfolio.items():
        value = stock_prices[stock] * quantity
        file.write(
            f"{stock} | Quantity: {quantity} | Value: ${value}\n"
        )

    file.write("\nTotal Investment: $" + str(total_investment))

print("\nPortfolio saved successfully in portfolio.txt!")
