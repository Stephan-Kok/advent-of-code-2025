import time
print("************* Day 2 *************")
start_time = time.time()
with open("input.txt", "r") as f:
    lines = f.readlines()

ids = []
for line in lines:
    id_list = line.split(',')
    for id in id_list:
        if id == '\n':
            continue
        id_set = id.split('-')
        ids.append((int(id_set[0]), int(id_set[1])))
    print(id_list)
print(ids)

# Simple walk
total = 0
for start, end in ids:
    for value in range(start, end + 1):
        x = str(value)
        if len(x) % 2 != 0:
            continue
        middle = int(len(x) / 2)
        if int(x[:middle]) == int(x[middle:]):
            # print(x)
            total += value


print("Done with part1: {}".format(total))
end_time = time.time()
print(f"Elapsed time: {end_time - start_time:.2f} seconds")


def check_valid(value):
    x = str(value)
    size = len(x)
    middle = int(size / 2)

    i = x[0]
    length = 1
    pos = 1
    while length <= middle:
        if (size % length) != 0:
            length += 1
            pos = length
            i = x[:length]
            continue

        while x[pos:pos + length] == i and pos + length <= size:
            pos += length
        if pos == size:
            # print("Invalid", value)
            return value
        length += 1
        pos = length
        i = x[:length]

    return -1

total2 = 0
for start, end in ids:
    for value in range(start, end + 1):
        result = check_valid(value)
        if result != -1:
            total2 += value



print("Done with part2: {}".format(total2))
end_time = time.time()
print(f"Elapsed time: {end_time - start_time:.2f} seconds")

# slower part2 but works
# def part2(value):
#     x = str(value)
#     size = len(x)
#     middle = int(len(x) / 2)
#     for i in range(1, middle + 1):
#         if size % i != 0:
#             continue
#         array = [x[index: index + i] for index in range(0, size, i)]
#         if all(chunk == array[0] for chunk in array):
#             return value
#     return -1
# total2 = 0
# for start, end in ids:
#     for value in range(start, end + 1):
#         # print("check", value)
#         result = part2(value)
#         if result != -1:
#             total2 += value
# print(total2)
# end_time = time.time()
# print(f"Elapsed time: {end_time - start_time:.2f} seconds")