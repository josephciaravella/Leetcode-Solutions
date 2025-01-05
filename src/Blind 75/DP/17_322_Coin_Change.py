def coinChange(coins, amount):
        tab = [len(coins)+1] * (amount+2)
        for coin in coins:
            if (coin == amount):
                return 1
            tab[coin] = 1

        i = 1
        while (i <= amount):
            if (i in coins):
                i += 1
                continue
            for coin in coins:
                if (tab[i-coin] > 0):
                    tab[i] = min(tab[i-coin] + 1, tab[i])
                else:
                    tab[i] = 0
            i +=1

        if (tab[amount] == 0):
            return -1
        else:
            return tab[amount]
        
print(coinChange([1], 0))