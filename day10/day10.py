import itertools
import time
import pulp

print("************* Day 10 *************")
start_time = time.time()

with open("input.txt", "r") as f:
    lines = f.readlines()

machines = []
for line in lines:
    machine = line.split("]")[0][1::]
    s_joltage_index = line.index("{")
    buttons = line[len(machine) + 2:s_joltage_index]
    buttons = [set([int(v) for v in b[1:-1].split(",")]) for b in buttons.strip().split(" ")]
    s_joltage = [int(v) for v in line.strip()[s_joltage_index + 1:-1].split(",")]
    machines.append((machine, buttons, s_joltage))


# symmetric difference, so adds if non existing and removes is existing
def press_button(state, button):
    return state ^ button

part1 = 0
for machine, buttons, _ in machines:
    solution = set([i for i, v in enumerate(machine) if v == '#'])
    # print("Machines: {} should be on: {} buttons: {}".format(machine, solution, buttons))

    # Brute force
    i = 1
    found = False
    while not found:
        combinations = list(itertools.combinations_with_replacement(buttons, i))
        # print("Checking {} combinations: {}".format(i, combintations))
        # print("combinations: {}".format(permutations))
        for combination in combinations:
            state = set()
            for button in combination:
                state = press_button(state, button)
            if state == solution:
                part1 += i
                found = True
                break
        i += 1
    # print("{} Machines: {} buttons: {} solution {}".format(len(combination), solution, buttons, combination))

print("Done with part1: {}".format(part1))
end_time = time.time()
print(f"Elapsed time: {end_time - start_time:.2e} seconds")

def joltage_press(state, buttons, solution, times):
    for button in buttons:
        state[button] += times
        if state[button] > solution[button]:
            raise ValueError("Value to high")
    return state

# Solve linear algebra AB=C where A is the button, X is the unknown presses and C is the joltage output
# (a1, b1)(x1) = (j1)
# (a2, b2)(x2) = (j1)
part2 = 0
for _, buttons, s_joltage in machines:
    # Create A
    A = [[0 for _ in range(len(buttons))] for _ in range(len(s_joltage))]
    for i in range(len(buttons)):
        button = buttons[i]
        for v in button:
            A[v][i] += 1
    C = s_joltage

    # Define problem (no objective, just feasibility)
    prob = pulp.LpProblem("AX_equals_C", pulp.LpMinimize)
    # Variables: x1..xn as integers
    x = [pulp.LpVariable(f"x{i}", lowBound=0, upBound=None, cat="Integer") for i in range(len(buttons))]
    # Add constraints: A @ x == C
    for i in range(len(C)):
        prob += pulp.lpSum(A[i][j] * x[j] for j in range(len(buttons))) == C[i]

    prob += pulp.lpSum(x)
    # Solve
    prob.solve(pulp.PULP_CBC_CMD(msg=False))

    solution = [pulp.value(var) for var in x]
    # print("Integer solution:", solution, sum(solution))
    part2 += sum(solution)

print("Done with part2: {}".format(int(part2)))
end_time = time.time()
print(f"Elapsed time: {end_time - start_time:.2e} seconds")