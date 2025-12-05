part1 = open(0).read().split("\n\n")[0]
ranges = sorted((*map(int, line.split("-")),) for line in part1.splitlines())

end = 0
result = 0
for r1, r2 in ranges:
    if r1 > end:
        end = r1 - 1
    if r2 > end:
        result += r2 - end
        end = r2

print(result)
