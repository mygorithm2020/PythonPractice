from copy import deepcopy
import random


num = 10
x = [None] * num

for i in range(num):
    x[i] = random.randint(1, num* 10)

print(x[:10])

x1 = deepcopy(x)
x1 = sorted(x1)
print(x1[:10])

x2 = sorted(x1, reverse=True)
print(x2[:10])