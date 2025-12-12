import re

parts = open(0).read().split("\n\n")

shapes = []
for part in parts[:-1]:
    shapes.append(part.splitlines()[1:])

regions = []
for line in parts[-1].splitlines():
    width, height, *numbers = map(int, re.findall("\\d+", line))
    regions.append((width, height, numbers))

result = 0
for width, height, numbers in regions:
    occupied = 0
    for i, num in enumerate(numbers):
        occupied += sum(row.count("#") for row in shapes[i]) * num
    if occupied <= width * height:
        result += 1

print(result)
