def describe_move(previous, current):
    if current > previous:
        return "UP"
    elif current < previous:
        return "DOWN"
    else:
        return "FLAT"

prices = [100, 98, 97, 101, 105, 105, 107, 102, 103, 99]

for index, price in enumerate(prices):
    if index == 0:
        continue
    previous_price = prices[index - 1]
    print(f"{previous_price} -> {price}: {describe_move(previous_price, price)}")

def get_moves(prices):
    moves = []
    for index, price in enumerate(prices):
        if index == 0:
            continue
        previous_price = prices[index - 1]
        moves.append(describe_move(previous_price, price))
    return moves

print(get_moves([100]))