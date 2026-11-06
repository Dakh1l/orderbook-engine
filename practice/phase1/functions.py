prices = [100, 98, 97, 101, 105, 105, 107, 102, 103, 99]
def describe_move(previous, current, show_percentage=False):
    if current > previous:
        move = "UP"
    elif current < previous:
        move = "DOWN"
    else:
        move = "FLAT"
    if show_percentage:
        if previous == 0:
            percentage_change = "N/A"
            return f"{move} ({percentage_change})"
        else:
            percentage_change = ((current - previous) / previous) * 100
        return f"{move} ({percentage_change:.2f}%)"
    return move

#for index, price in enumerate(prices):
    #if index == 0:
        #continue
    #previous_price = prices[index - 1]
    #print(f"{previous_price} -> {price}: {describe_move(previous_price, price, show_percentage=True)}")

def get_moves(prices, show_percentage=False):
    moves = []
    for index, price in enumerate(prices):
        if index == 0:
            continue
        previous_price = prices[index - 1]
        moves.append(describe_move(previous_price, price, show_percentage))
    return moves

#print(describe_move(0, 105, show_percentage=True))
print(get_moves(prices))