import time
print("************* Day 4 *************")
start_time = time.time()

with open("input.txt", "r") as f:
    lines = f.readlines()

for line in lines:
    print(line[:-1])


height=(len(lines))
width=len(lines[0]) - 1
# print(height,width)

matrix=[]
for y in range(height):
    line = []
    for x in range(width):
        line.append(lines[y][x])
    matrix.append(line)

for line in matrix:
    print(line)

def save_check(y,x):
    if 0 <= x < width and 0 <= y < height:
        #print(y,x, lines[y][x], lines[y][x] == '@')
        return matrix[y][x] == '@'
    return False

def count_neighbours(y,x):
    count = 0
    #print("Check", y,x , "******")
    for y1 in range(y-1,y+2):
        for x1 in range(x-1,x+2):
            if y1 == y and x1 == x:
                continue
            else:
                if save_check(y1,x1):
                    count += 1
                    if count > 3:
                        return True


    return False
# print("***")
part1 = 0
for y in range(height):
    line = ""
    for x in range(width):
        if matrix[y][x] == "@":
            if not count_neighbours(y,x):
                line += "x"
                part1 += 1
            else:
                line += "@"
        else:
            line += "."
            # paper_roles["{y}-{x}".format(y=y, x=x)] = True
    # print(line)

# print(paper_roles)

print("Done with part1: {}".format(part1))
end_time = time.time()
print(f"Elapsed time: {end_time - start_time:.2e} seconds")

round=0
part2 = 0
tmp = -1
while (tmp != part2):
    print("Round {}".format(round))
    round += 1
    tmp = part2
    for y in range(height):
        line = ""
        for x in range(width):
            if matrix[y][x] == "@":
                if not count_neighbours(y,x):
                    line += "x"
                    matrix[y][x] = "."
                    part2 += 1
                else:
                    line += "@"
            else:
                line += "."
print("Done with part2: {}".format(part2))
end_time = time.time()
print(f"Elapsed time: {end_time - start_time:.2e} seconds")