import time
print("************* Day 1 *************")
start = time.time()
with open("input.txt", "r") as f:
    lines = f.readlines()

class Lock:
    def __init__(self):
        # self.prev = 50
        self.pos = 50
        self.result = 0

    def step(self, step):
        direction = step[0]
        count = int(step[1:])
        if direction == "R":
            self.pos = (self.pos + count) % 100
        elif direction == "L":
            self.pos = (self.pos - count) % 100

    def password_method(self, step):
        # self.prev = self.pos, self.result
        direction = step[0]
        count = int(step[1:])

        # Calculate and remove useless rotations
        self.result += int(count / 100)
        count = count % 100

        if direction == "R":
            # if rotated over 99 - count 1
            if ((self.pos + count) % 100) != (self.pos + count):
                self.result += 1
            self.pos = (self.pos + count) % 100
        elif direction == "L":
            # if didnt start at 0 and [ rotated over 0 or ended at 0 ] - count 1
            if (self.pos != 0 and ((self.pos - count) % 100) != (self.pos - count) or (self.pos - count) == 0):
                self.result += 1
            self.pos = (self.pos - count) % 100

lock = Lock()
result = 0
for line in lines:
    prev = lock.pos
    lock.password_method(line.strip())
    # print(line.strip(), prev, '->', lock.pos, lock.result)
    if lock.pos == 0:
        result += 1
print("Done with part1: {}".format(result))
end = time.time()
print(f"Elapsed time: {end - start:.2e} seconds")
print("Done with part2: {}".format(lock.result))
end = time.time()
print(f"Elapsed time: {end - start:.2e} seconds")
