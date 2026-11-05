prices = [100, 98, 97, 101, 105, 105, 107, 102, 103, 99]
for index, price in enumerate(prices):
    if index == 0:
        continue
    if price > prices[index - 1]:
        print(f"Price increased from {prices[index - 1]} to {price} which is an increase of {(price - prices[index - 1])/prices[index - 1] * 100:.2f}%.")
    elif price < prices[index - 1]:
        print(f"Price decreased from {prices[index - 1]} to {price} which is a decrease of {(prices[index - 1] - price)/prices[index - 1] * 100:.2f}%.")
    elif price == prices[index - 1]:
        print(f"Price remained the same at {price}.")