import random
lotteryNumbers = []

for i in range(6):
    i = random.randint(1, 38)
    while i in lotteryNumbers:
        i = random.randint(1, 38)
    lotteryNumbers.append(i)

lotteryNumbers.sort()
print(lotteryNumbers)

special = []
for j in range(1):
    j = random.randint(1, 8)
    special.append(j)

print(special)

