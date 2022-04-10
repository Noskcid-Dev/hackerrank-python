from itertools import combinations

x, y = input().split()

for i in range(1, int(y)+1):
    for z in combinations(sorted(x), i):
        print(''.join(z))
        