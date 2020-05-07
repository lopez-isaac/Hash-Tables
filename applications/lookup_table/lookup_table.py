import math
import random

# def slowfun(x, y):
#     # TODO: Modify to produce the same results, but much faster
#     v = math.pow(x, y)
#     v = math.factorial(v)
#     v //= (x + y)
#     v %= 982451653
#
#     return v

#My Way

# cache = {}
#
# def fastfun(x, y):
#     if x not in cache:
#         cache[x] = math.pow(x, y)
#         cache[x] = math.factorial(cache[x])
#         cache[x] //= (x + y)
#         cache[x] %= 982451653
#     return cache[x]

#another way
cache = {}
def build_lookup_table(x, y):
    for x, y in range(2, 15):
        slowfun(x, y)
def slowfun(x, y):
    # TODO: Modify to produce the same results, but much faster
    v = (x, y)
    if (x,y) not in cache:
        cache[v] = math.pow(x, y)
        cache[v] = math.factorial(cache[v])
        cache[v] //= (x + y)
        cache[v] %= 982451653
    return cache[v]


# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
