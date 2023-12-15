import time
import itertools
f = open("input.txt", "r")

s = time.time()

lines = f.readlines()
instructions = lines.pop(0).strip()
instructions = instructions.replace("L", "0").replace("R", "1")

paths = {}
for line in lines:
    line = line.strip().split(" = ")
    value = line[1].replace("(", "").replace(")", "").split(", ")
    paths[line[0]] = value

steps = 0
location = "AAA"
for instruction in itertools.cycle(instructions):
    instruction = int(instruction)
    steps += 1
    location = paths[location][instruction]
    if location == "ZZZ":
        break

e = time.time()
print(f"My method found: {steps} in {e - s}s")
