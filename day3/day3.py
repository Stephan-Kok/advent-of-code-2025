import time
print("************* Day 3 *************")
start_time = time.time()

with open("input.txt", "r") as f:
    lines = f.readlines()

battery = []
for line in lines:
    bank = []
    for char in line:
        if char.isdigit():
            bank.append(int(char))
    battery.append(bank)


part1 = 0
for bank in battery:
    m1 = max(bank[:-1])
    i1 = bank.index(m1)
    m2 = max(bank[i1+1:])
    jolts = int(str(m1) + str(m2))
    part1 += jolts


print("Done with part1: {}".format(part1))
end_time = time.time()
print(f"Elapsed time: {end_time - start_time:.2e} seconds")

def voltage(bank, digits):
    if (digits == 1):
        m = max(bank)
    else:
        m = max(bank[:-(digits - 1)])
    i = bank.index(m)
    return (m, i)

part2 = 0
for bank in battery:
    bank_index = 0
    jolts = ""
    for i in range(12,0,-1):
        m, index = voltage(bank[bank_index:], i)
        bank_index += index + 1
        jolts += str(m)
    part2 += int(jolts)


print("Done with part2: {}".format(part2))
end_time = time.time()
print(f"Elapsed time: {end_time - start_time:.2e} seconds")