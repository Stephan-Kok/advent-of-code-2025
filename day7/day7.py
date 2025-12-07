import time
import operator
import re

print("************* Day 7 *************")
start_time = time.time()

with open("input.txt", "r") as f:
    lines = f.readlines()

height = len(lines) - 1
width = len(lines[0]) - 1
splitters = {}
timelines = {}

for y in range(height):
    for x in range(width):
        if lines[y][x] == "S":
            start = (y,x)
        if lines[y][x] == "^":
            splitters["{}-{}".format(y,x)] = False

def check_path(pos):
    y, x = pos[0] + 1, pos[1]
    if lines[y][x] == "^":
        splitters["{}-{}".format(y, x)] = True
        return [(y, x - 1), (y, x + 1)]
    return [(y,x)]

# walk
positions = set([start])
timelines["{}-{}".format(start[0], start[1])] = 1
for i in range(height):
    if i == height - 1:
        part2_list = []

    next_positions = set()
    for pos in positions:
        result = check_path(pos)
        next_positions.update(result)
        for (y,x) in result:
            key = "{}-{}".format(y, x)
            if i == height - 1:
                part2_list.append(key)
            prev_key = "{}-{}".format(pos[0], pos[1])
            if key in timelines:
                timelines[key] += timelines[prev_key]
            else:
                timelines[key] = timelines[prev_key]
    positions = next_positions

# print(timelines)

part1 = 0
for split in splitters.values():
    if split:
        part1 += 1


print("Done with part1: {}".format(part1))
end_time = time.time()
print(f"Elapsed time: {end_time - start_time:.2e} seconds")

part2 = 0
for key in part2_list:
    part2 += timelines[key]

print("Done with part2: {}".format(part2))
end_time = time.time()
print(f"Elapsed time: {end_time - start_time:.2e} seconds")

# Print result of part2
# for y in range(height):
#     line = ""
#     for x in range(width):
#         key = "{}-{}".format(y, x)
#         if key in timelines:
#             line += str(timelines[key])
#         else:
#             line += lines[y][x]
#     print(line)