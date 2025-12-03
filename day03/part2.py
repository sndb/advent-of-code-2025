def solve(b, n):
    if n == 0:
        return ""

    for i in range(9, -1, -1):
        idx = b.find(str(i))
        if idx != -1 and len(b) - idx >= n:
            return str(i) + solve(b[idx + 1 :], n - 1)

batteries = open(0).read().splitlines()
print(sum(int(solve(b, 12)) for b in batteries))
