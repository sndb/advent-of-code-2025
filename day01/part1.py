data = [(x[0], int(x[1:])) for x in open(0).read().splitlines()]
curr, result = 50, 0

for d, n in data:
    curr += n if d == "R" else -n
    result += curr % 100 == 0

print(result)
