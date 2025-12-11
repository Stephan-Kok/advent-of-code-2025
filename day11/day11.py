import time
from functools import cache

print("************* Day 11 *************")
start_time = time.time()

with open("input.txt", "r") as f:
    lines = f.readlines()

nodes = {}
for line in lines:
    key = line[0:3]
    values = line[5:-1].split(" ")
    nodes[key] = values

positions = nodes["you"]
part1 = 0
while len(positions) > 0:
    new_position = []
    for position in positions:
        if nodes[position] != ["out"]:
            new_position.extend(nodes[position])
        else:
            part1 += 1
    positions = new_position

print("Done with part1: {}".format(int(part1)))
end_time = time.time()
print(f"Elapsed time: {end_time - start_time:.2e} seconds")

@cache
def recursive_check(node, fft_visited, dac_visited):
    if node == "fft":
        fft_visited = True
    if node == "dac":
        dac_visited = True
    if node == "out":
        if fft_visited and dac_visited:
            return 1
        return 0
    else:
        return sum(recursive_check(next_node, fft_visited, dac_visited) for next_node in nodes[node])

part2 = recursive_check("svr", False, False)

print("Done with part2: {}".format(int(part2)))
end_time = time.time()
print(f"Elapsed time: {end_time - start_time:.2e} seconds")
