def solve(b):
    high = 0
    result = 0
    for c in b:
        result = max(result, high * 10 + int(c))
        high = max(high, int(c))
    return result

batteries = open(0).read().splitlines()
print(sum(solve(b) for b in batteries))
