#variable declaration
import random

numberOfStreaks = 0
CoinFlip = []
streak = 0

for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    for i in range(100):
        CoinFlip.append(random.randint(0,1))
    #does not matter if it is 0 or 1, H or T, peas or lentils. I am going to check if there is multiple 0 or 1 in a row

    # Code that checks if there is a streak of 6 heads or tails in a row.
    for i in range(1,len(CoinFlip)):
        if CoinFlip[i] == CoinFlip[i-1]:  #checks if current list item is the same as before
            streak += 1
        else:
            streak = 0

        if streak > 0:
            numberOfStreaks += 1

    CoinFlip = []


print('Chance of streak: %s%%' % (numberOfStreaks / 1000000))
