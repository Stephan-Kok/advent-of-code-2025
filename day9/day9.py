import time
import itertools

print("************* Day 9 *************")
start_time = time.time()

with open("input.txt", "r") as f:
    lines = f.readlines()

points = []
for line in lines:
    tmp = line.split(",")
    box = (int(tmp[0]), int(tmp[1]))
    points.append(box)

combinations = list(itertools.combinations(points, 2))
print("Calculating the distance between permutations of {} boxes".format(len(combinations)))

database = {}
for (x1,y1), (x2, y2) in combinations:
    area = (max(x1, x2) - min(x1, x2) + 1) * (max(y1, y2) - min(y1, y2) + 1)
    database[area] = (x1,y1), (x2, y2)
keys = sorted(database, key=float, reverse=True)
part1 = keys[0]

print("Done with part1: {}".format(part1))
end_time = time.time()
print(f"Elapsed time: {end_time - start_time:.2e} seconds")

# Show image!
# import matplotlib.pyplot as plt
#
# # Example list of points
# # points = [(2, 3), (4, 7), (6, 1), (8, 5)]
#
# # Separate x and y coordinates
# x_vals = [x for x, y in points]
# y_vals = [y for x, y in points]
#
# # Create scatter plot
# plt.scatter(x_vals, y_vals, color="blue", marker="o", label="Points")
#
# # Optionally connect them with a line
# plt.plot(x_vals, y_vals, color="gray", linestyle="--")
#
# # Add labels and title
# plt.xlabel("X-axis")
# plt.ylabel("Y-axis")
# plt.title("Plot of Points")
# plt.legend()
#
# # Show the graph
# plt.show()

boundary = set(points)
for i in range(len(points)):
    x1, y1 = points[i]
    x2, y2 = points[(i + 1) % len(points)]
    if x1 == x2:
        xstep = 1 if y2 > y1 else -1
        for y in range(y1, y2 + xstep, xstep):
            boundary.add((x1, y))
    else:
        xstep = 1 if x2 > x1 else -1
        for x in range(x1, x2 + xstep, xstep):
            boundary.add((x, y1))
# print(boundary)

# For quick corner checks, calculate max xvalues for all y
polygon = {}
for x, y in boundary:
    if y in polygon:
        minx, maxx = polygon[y]
        polygon[y] = (min(minx, x), max(maxx, x))
    else:
        polygon[y] = (x, x)

# for y in range(9):
#     line = ""
#     for x in range(15):
#         if (x, y) in boundary:
#             if (x, y) == (11, 7) or (x, y) == (10,7):
#                 line += "O"
#             else:
#                 line += "#"
#         else:
#             line += "."
#     print(line)

def walk(x1, y1, x2, y2):
    # Check if corners inside
    if y1 not in polygon or y2 not in polygon:
        return False
    if x2 < polygon[y1][0] or x2 > polygon[y1][1]:
        return False
    if x1 < polygon[y2][0] or x1 > polygon[y2][1]:
        return False

    xstep = 1 if x2 > x1 else -1
    ystep = 1 if y2 > y1 else -1
    # Check from x1 -> x2 at y1
    # print("Check {} -> {} at y1".format(x1,x2), xstep)
    inbound = False
    for x in range(x1 + xstep, x2 + xstep, xstep):
        if (x, y1) in boundary:
            inbound = True
            # print("In boundry ({},{})".format(x, y1))
        else:
            if inbound:  # exited boundary check if boundary got larger or smaller
                inbound = False
                if (x - xstep, y1 + ystep) in boundary:
                    # print("Not a square exit  ({},{})".format(x, y1))
                    return False
                elif (x - xstep, y1 - ystep) in boundary:
                    # print("Boundry is larger its oke")
                    continue
                else:
                    print("what? ({},{})".format(x, y1))
            inbound = False
    # Check from y1 -> y2 at x1
    # print("Check {} -> {} at x1".format(y1, y2), ystep)
    inbound = False
    for y in range(y1 + ystep, y2 + ystep, ystep):
        if (x1, y) in boundary:
            inbound = True
            # print("In boundry ({},{})".format(x1, y))
        else:
            if inbound:  # exited boundary check if boundary got larger or smaller
                inbound = False
                if (x1 + xstep, y - ystep) in boundary:
                    # print("Not a square exit ({},{})".format(x1, y))
                    return False
                elif (x1 - xstep, y - ystep) in boundary:
                    # print("Boundry is larger its oke")
                    continue
                else:
                    print("what? ({},{})".format(x1, y))
            inbound = False
    # other point

    xstep = -xstep
    ystep = -ystep
    # check x2 -> x1 at y2
    # print("Check {} -> {} at y2".format(x2, x1), xstep)
    inbound = False
    for x in range(x2 + xstep, x1 + xstep, xstep):
        if (x, y2) in boundary:
            inbound = True
            # print("In boundry ({},{})".format(x, y2))
        else:
            if inbound:  # exited boundary check if boundary got larger or smaller
                inbound = False
                if (x - xstep, y2 + ystep) in boundary:
                    # print("Not a square exit  ({},{})".format(x, y2))
                    return False
                elif (x - xstep, y2 - ystep) in boundary:
                    # print("Boundry is larger its oke")
                    continue
                else:
                    print("what? ({},{})".format(x, y2))
            inbound = False
    # Check from y2 -> y1 at x2
    # print("Check {} -> {} at x2".format(y2, y1), ystep)
    inbound = False
    for y in range(y2 + ystep, y1 + ystep, ystep):
        if (x2, y) in boundary:
            inbound = True
            # print("In boundry ({},{})".format(x2, y))
        else:
            if inbound:  # exited boundary check if boundary got larger or smaller
                inbound = False
                if (x2 + xstep, y - ystep) in boundary:
                    # print("Not a square exit ({},{})".format(x2, y))
                    return False
                elif (x2 - xstep, y - ystep) in boundary:
                    # print("Boundry is larger its oke")
                    continue
                else:
                    print("what? ({},{})".format(x2, y))
            inbound = False
    return True

for key in keys:
    (x1, y1), (x2, y2) = database[key]

    # print("Checking ({},{})-({},{}): {}".format(x1,y1,x2,y2,key))
    # traverse line
    if walk(x1, y1, x2, y2):
        part2 = key
        break
    else:
        continue


print("Done with part2: {}".format(part2))
end_time = time.time()
print(f"Elapsed time: {end_time - start_time:.2e} seconds")
