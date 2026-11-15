
# Stock Portfolio Tracker

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190
}

portfolio = {}
total_investment = 0

print("================================")
print("      STOCK PORTFOLIO TRACKER")
print("================================")

print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock} : Rs.{price}")

# Get number of stocks
n = int(input("\nHow many stocks do you want to add? "))

# Get stock details
for i in range(n):
    stock = input("\nEnter stock symbol: ").upper()

    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be positive.")
            continue

        portfolio[stock] = portfolio.get(stock, 0) + quantity

        investment = stock_prices[stock] * quantity
        total_investment += investment

        print("Stock added successfully!")

    else:
        print("Invalid stock symbol!")

# Display portfolio
print("\n========== YOUR PORTFOLIO ==========")

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    value = price * quantity

    print(f"{stock} | Quantity: {quantity} | "
          f"Price: Rs.{price} | Value: Rs.{value}")

print("-----------------------------------")
print(f"Total Investment: Rs.{total_investment}")
print("===================================")

# Save result to a text file
with open("portfolio.txt", "w") as file:
    file.write("STOCK PORTFOLIO REPORT\n")

    for stock, quantity in portfolio.items():
        value = stock_prices[stock] * quantity
        file.write(f"{stock}: Quantity = {quantity}, "
                   f"Value = Rs.{value}\n")

    file.write(f"\nTotal Investment: Rs.{total_investment}")

print("\nPortfolio saved successfully!")
