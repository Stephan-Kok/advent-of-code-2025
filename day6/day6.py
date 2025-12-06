import time
import operator
import re

print("************* Day 6 *************")
start_time = time.time()

with open("input.txt", "r") as f:
    lines = f.readlines()

math = []
operations = []
for i in range(0, len(lines)):
    splitted = re.split(r'[ ]+', lines[i])
    if i == len(lines) - 1:
        operations = [operator.add if x == "+" else operator.mul for x in splitted]
        break
    if splitted[0] == "":
        splitted.remove("")
    numbers = [int(x) for x in splitted]
    math.append(numbers)
# print(math)
# print(operations)

def calculate(index, op, database):
    result = database[0][index]
    for i in range(1, len(math)):
        n = database[i][index]
        result = op(n, result)
    return result

part1 = 0
for i in range(0, len(operations)):
    part1 += calculate(i, operations[i], math)

print("Done with part1: {}".format(part1))
end_time = time.time()
print(f"Elapsed time: {end_time - start_time:.2e} seconds")

height = len(lines) - 1
width = len(lines[0])
numbers = []
question = []
for x in range(0, width):
    row = ""
    for y in range(height):
        try:
            v = lines[y][x]
        except IndexError:
            v = " "
        row += v
    row = row.strip()
    if row.isdigit():
        question.append(int(row))
    else:
        numbers.append(question)
        question = []
numbers.append(question)
# print(numbers)

def calculate2(row, op):
    result = row[0]
    for i in range(1, len(row)):
        n = row[i]
        result = op(n, result)
    return result

part2 = 0
for i in range(0, len(operations)):
    part2 += calculate2(numbers[i], operations[i])



print("Done with part2: {}".format(part2))
end_time = time.time()
print(f"Elapsed time: {end_time - start_time:.2e} seconds")
