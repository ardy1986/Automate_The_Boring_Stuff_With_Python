import random

req_streak = int(input('How many streaks you need?\n'))
num_of_streak = 0

for j in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' value
    coin_flip = []
    streak = 0
    for k in range(100):
        if random.randint(0,1) == 0:
            coin_flip += 'H'
        else:
            coin_flip += 'T'
        # Code that check if there is a streak of 6 heads or tails in a row
        if k > 0 and coin_flip[k] == coin_flip[k-1]:
            streak += 1
        else:
            streak = 0
        if streak > (req_streak - 2) :
            num_of_streak += 1

#print(coin_flip)
print('Number of ' + str(req_streak) +' consecutive streaks in 100000 trials is '+ str(num_of_streak))
print('Chance of streak: %s%%' % (num_of_streak/10000/(100-req_streak-1)*100))
