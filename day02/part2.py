ids = [tuple(map(int, x.split("-"))) for x in input().split(",")]

result = 0
for r1, r2 in ids:
    for i in range(r1, r2 + 1):
        s = str(i)
        for n in range(1, len(s) // 2 + 1):
            for m in range(n, len(s), n):
                if s[:n] != s[m : m + n]:
                    break
            else:
                result += i
                break

print(result)
