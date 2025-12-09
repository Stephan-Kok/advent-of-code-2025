import time
import math
import itertools

print("************* Day 8 *************")
start_time = time.time()

with open("input.txt", "r") as f:
    lines = f.readlines()

boxes = []
for line in lines:
    tmp = line.split(",")
    box = (int(tmp[0]), int(tmp[1]), int(tmp[2]))
    boxes.append(box)

permutations = list(itertools.permutations(boxes, 2))
print("Calculating the distance between permutations of {} boxes".format(len(permutations)))

database = {}
for p1, p2 in permutations:
    distance = math.dist(p1, p2)
    database[distance] = (p1, p2)
keys = sorted(database, key=float)

iterations = 1000
print("Creating circuits with {} keys and {} iterations".format(len(keys), iterations))
circuits = []
for i in range(iterations):
    box1, box2 = database[keys[i]]
    found = False
    prev = None
    for circuit in circuits:
        if box1 in circuit or box2 in circuit:
            if found:
                # print("should merge")
                circuits.remove(circuit)
                prev.update(circuit)
            else:
                circuit.update([box1, box2])
                prev = circuit
                found = True
    if not found:
        circuits.append({box1, box2})
    # print("Circuit #{}: {}".format(box1, box2))
    # print(circuits)

circuits = sorted(circuits, key=len, reverse=True)

part1 = 1
for i in range(3):
    part1 *= len(circuits[i])
    print(len(circuits[i]), circuits[i])

# def find_closest(boxes):
#
# print(boxes)
# print(database)
#
# keys = database.keys()
# sorted_keys = sorted(keys, key=float)
# print(sorted_keys)
# for i in range(len(sorted_keys) - 1):
#     print(math.dist(database[sorted_keys[i]], database[sorted_keys[i + 1]]))


print("Done with part1: {}".format(part1))
end_time = time.time()
print(f"Elapsed time: {end_time - start_time:.2e} seconds")

part2 = 0
finished = len(boxes)
i = iterations
while len(circuits[0]) != finished:
    box1, box2 = database[keys[i]]
    found = False
    prev = None
    for circuit in circuits:
        if box1 in circuit or box2 in circuit:
            if found:
                # print("should merge")
                circuits.remove(circuit)
                prev.update(circuit)
            else:
                circuit.update([box1, box2])
                prev = circuit
                found = True
    if not found:
        circuits.append({box1, box2})
    i += 1
part2 = box1[0] * box2[0]

print("Done with part2: {}".format(part2))
end_time = time.time()
print(f"Elapsed time: {end_time - start_time:.2e} seconds")