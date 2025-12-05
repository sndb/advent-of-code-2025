part1, part2 = open(0).read().split("\n\n")
ranges = [(*map(int, line.split("-")),) for line in part1.splitlines()]
numbers = [int(line) for line in part2.splitlines()]
print(sum(any(r1 <= n <= r2 for r1, r2 in ranges) for n in numbers))
