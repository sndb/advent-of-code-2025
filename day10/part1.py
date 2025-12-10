from math import inf

machines = []
for line in open(0).read().splitlines():
    lights, *buttons, _ = line.split()
    lights = {i for i, l in enumerate(lights[1:-1]) if l == "#"}
    buttons = [[int(c) for c in button[1:-1].split(",")] for button in buttons]
    machines.append((lights, buttons))

def solve(machine, lights, idx, acc):
    goal, buttons = machine
    if goal == lights:
        return acc

    if idx == len(buttons):
        return inf

    s1 = solve(machine, lights, idx + 1, acc)
    s2 = solve(machine, lights ^ set(buttons[idx]), idx + 1, acc + 1)
    return min(s1, s2)

print(sum(solve(m, set(), 0, 0) for m in machines))
