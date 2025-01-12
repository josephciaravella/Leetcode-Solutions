def coinChange(coins, amount):
    tab = [amount + 1] * (amount + 1)
    tab[0] = 0

    for coin in coins:
        if coin <= amount:
            tab[coin] = 1

    i = 1
    while i <= amount:
        for coin in coins:
            if i - coin >= 0:
                tab[i] = min(tab[i], tab[i-coin] + 1)
        i += 1

    if tab[amount] == amount + 1:
        return -1
    else:
        return tab[amount]
        
print(coinChange([1], 0))