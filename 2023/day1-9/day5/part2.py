import time

f = open("input.txt", "r")

s = time.time()

info = [[], [], [], [], [], [], [], []]

i = 0
for line in f:
    line = line.strip()

    if line == "":
        i += 1
        continue

    if line[0].isalpha():
        continue

    info[i].append(line.split())

seed_ranges = info.pop(0)
seeds = []

for x in range(int(len(seed_ranges[0]) / 2)):
    for y in range(int(seed_ranges[0][(x * 2) + 1])):
        seeds.append(int(seed_ranges[0][x * 2]) + y)

print(seeds)  # <------------ Code doesn't even get to here before throwing memory error lol I have no idea

lowest = 999999999999999999999999999999999

for seed in seeds:
    curr = seed
    for x in range(len(info)):
        for y in range(len(info[x])):
            if int(info[x][y][1]) <= curr < int(info[x][y][1]) + int(info[x][y][2]):
                curr = int(info[x][y][0]) + (curr - int(info[x][y][1]))
                break

    if curr < lowest:
        print("best seed", seed)
        lowest = curr

e = time.time()

print(f"My method found: {lowest} in {e - s}s")
