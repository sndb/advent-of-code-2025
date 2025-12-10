import z3

machines = []
for line in open(0).read().splitlines():
    _, *buttons, counters = line.split()
    buttons = [[int(c) for c in button[1:-1].split(",")] for button in buttons]
    counters = [int(c) for c in counters[1:-1].split(",")]
    machines.append((buttons, counters))

def solve(machine):
    buttons, counters = machine

    solver = z3.Optimize()

    presses = [z3.Int(f"p{b}") for b in enumerate(buttons)]
    for p_i in presses:
        solver.add(p_i >= 0)

    for c, counter in enumerate(counters):
        c_i = z3.Int(f"c{c}")
        solver.add(c_i == counter)
        solver.add(c_i == z3.Sum(presses[b] for b, cs in enumerate(buttons) if c in cs))

    total = z3.Int("t")
    solver.add(total == z3.Sum(*presses))
    solver.minimize(total)

    solver.check()
    return solver.model()[total].py_value()

print(sum(map(solve, machines)))
