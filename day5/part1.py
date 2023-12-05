f = open("input.txt", "r")

ans = 0

info = [[],[],[],[],[],[],[],[]]

i = 0
for line in f:
    line = line.strip()

    if line == "":
        i += 1
        continue

    if line[0].isalpha():
        continue

    info[i].append(line)

for x in range(len(info)):
    for element in info[x]:
        
