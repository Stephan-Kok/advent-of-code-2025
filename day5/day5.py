import time

print("************* Day 5 *************")
start_time = time.time()

with open("input.txt", "r") as f:
    lines = f.readlines()

database = []
i = 0
for i in range(0, len(lines)):
    line = lines[i]
    fresh = line.split("-")
    if len(fresh) != 2:
        break
    database.append((int(fresh[0]), int(fresh[1])))

# for x,y in database:
#     print("{}-{}".format(x,y))

i += 1
products = []
for j in range(i, len(lines)):
    line = lines[j]
    products.append(int(line))

# print()
# for product in products:
#     print(product)

# Sort database and then merge them for part2
db = database
db.sort(key=lambda p: p[0])
i = 0
while (i < len(db) - 1):
    x, y = db[i]
    x2, y2 = db[i + 1]

    if y >= x2:
        db.remove((x2, y2))
        db[i] = (x, max(y, y2))
        i -= 1
    i += 1

def is_fresh(product, database):
    for x, y in database:
        if x <= product <= y:
            return True
    return False

part1 = 0
for product in products:
    if is_fresh(product, db):
        part1 += 1

print("Done with part1: {}".format(part1))
end_time = time.time()
print(f"Elapsed time: {end_time - start_time:.2e} seconds")

part2 = 0
for x,y in db:
    part2 += y - x + 1

print("Done with part2: {}".format(part2))
end_time = time.time()
print(f"Elapsed time: {end_time - start_time:.2e} seconds")