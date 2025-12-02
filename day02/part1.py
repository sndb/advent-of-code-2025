ids = [tuple(map(int, x.split("-"))) for x in input().split(",")]

result = 0
for r1, r2 in ids:
    for i in range(r1, r2 + 1):
        s = str(i)
        if s[: len(s) // 2] == s[len(s) // 2 :]:
            result += i

print(result)
