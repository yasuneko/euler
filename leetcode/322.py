
def coinChange(coins, amount):
    store = [-2] * (amount + 1)
    @profile
    def stuff(coins, amount):
        if amount < 0:
            return -1
        if amount == 0:
            return 0
        else:
            if store[amount] > -2:
                return store[amount]
            else:
                min_coins = -1
                for coin in coins:
                    #print amount, coin, amount - coin
                    num_coins = stuff(coins, amount - coin)
                    if num_coins > -1:
                        num_coins += 1
                        if min_coins == -1 or num_coins < min_coins:
                            min_coins = num_coins
                store[amount] = min_coins
                return min_coins

    return stuff(coins, amount)

#print coinChange([4,5], 11)

#print coinChange([186,419,83,408], 6249)

print coinChange([70,177,394,428,427,437,176,145,83,370],7582)
