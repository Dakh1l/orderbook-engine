prices = [100, 98, 97, 101, 105, 105, 107, 102, 103, 99]
def describe_move(previous, current, show_percentage=False):
    if current > previous:
        return "UP"
    elif current < previous:
        return "DOWN"
    else:
        return "FLAT"
    if show_percentage == True:
        percentage_change = ((current - previous) / previous) * 100
        return f"{describe_move(previous, current)} ({percentage_change:.2f}%)" 

for index, price in enumerate(prices):
    if index == 0:
        continue
    previous_price = prices[index - 1]
    print(f"{previous_price} -> {price}: {describe_move(previous_price, price, show_percentage=True)}")

def get_moves(prices):
    moves = []
    for index, price in enumerate(prices):
        if index == 0:
            continue
        previous_price = prices[index - 1]
        moves.append(describe_move(previous_price, price, show_percentage=True))
    return moves

print(get_moves([100, 98, 97, 101, 105, 105, 107, 102, 103, 99]))