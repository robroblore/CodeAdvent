f = open("input.txt", "r")
engine = []
gears = {}

ans = 0


def checkNeighbours(l, index, num):
    # Checks left and right
    if index > 0 and engine[l][index - 1] != '.':
        if f"{l}:{index - 1}" in gears:
            gears[f"{l}:{index - 1}"].append(int(num))
        else:
            gears[f"{l}:{index - 1}"] = [int(num)]

    if index + len(num) < len(engine[l]) - 1 and engine[l][index + len(num)] != '.':
        if f"{l}:{index + len(num)}" in gears:
            gears[f"{l}:{index + len(num)}"].append(int(num))
        else:
            gears[f"{l}:{index + len(num)}"] = [int(num)]

    # Checks above
    if l > 0:
        for x in range(len(num) + 2):
            check = index-1+x
            if (check >= 0) and (check < len(engine[l-1])) and (engine[l-1][check] != '.') and (not engine[l-1][check].isnumeric()):
                if f"{l - 1}:{check}" in gears:
                    gears[f"{l-1}:{check}"].append(int(num))
                else:
                    gears[f"{l-1}:{check}"] = [int(num)]

    # Checks below
    if l < len(engine)-1:
        for x in range(len(num) + 2):
            check = index-1+x
            if (check >= 0) and (check < len(engine[l+1])) and (engine[l+1][check] != '.') and (not engine[l+1][check].isnumeric()):
                if f"{l + 1}:{check}" in gears:
                    gears[f"{l + 1}:{check}"].append(int(num))
                else:
                    gears[f"{l + 1}:{check}"] = [int(num)]

    return 0


for line in f:
    engine.append(line.strip())

for l in range(len(engine)):
    counting = False
    num = ""
    for index, value in enumerate(engine[l]):
        if not value.isnumeric():
            if counting:
                counting = False
                checkNeighbours(l, startIndex, num)
                num = ""
            continue

        if not counting:
            startIndex = index

            counting = True
        num += value

        if index == len(engine[l])-1:
            counting = False
            checkNeighbours(l, startIndex, num)
            num = ""

for value in gears.values():
    if len(value) == 2:
        ans += value[0] * value[1]

print(gears)
print(ans)
