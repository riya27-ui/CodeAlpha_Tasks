stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGLE": 150,
    "MSFT": 300,
    "NIFTY": 200,
    "TATA": 500,
    "Reliance": 450
}

total = 0

print("Stock Portfolio Tracker 📈")

while True:
    stock = input("\nEnter stock name (or type DONE): ").upper()

    if stock == "DONE":
        break

    if stock in stocks:
        quantity = int(input("Enter quantity: "))

        investment = stocks[stock] * quantity
        total += investment

        print(f"✅ Added {stock}")
        print(f"Investment Value: ${investment}")

    else:
        print("❌ Stock not found!")

print("\n📊 Portfolio Summary")
print("Total Portfolio Value: $", total)