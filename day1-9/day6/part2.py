import time

# Literally same code as part 1 hahaha

f = open("input.txt", "r")

ans = 1

s = time.time()

times = f.readline().strip().split()
distances = f.readline().strip().split()
times.pop(0)
distances.pop(0)

# dist = hold_time * (time - hold_time)

for t in range(len(times)):
    ti = int(times[t])
    for hold_time in range(1, ti):
        dist = hold_time * (ti - hold_time)
        if dist > int(distances[t]):
            lowest_hold_time = hold_time
            ans *= ti-lowest_hold_time-lowest_hold_time+1
            break

e = time.time()
print(f"My method found: {ans} in {e - s}s")
