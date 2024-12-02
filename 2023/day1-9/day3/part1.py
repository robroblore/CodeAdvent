f = open("input.txt", "r")
engine = []
ans = 0


def checkNeighbours(l, index, num):
    global ans
    # Checks left and right
    if (
            (index > 0 and engine[l][index - 1] != '.') or
            (index + len(num) < len(engine[l]) - 1 and engine[l][index + len(num)] != '.')
    ):
        return int(num)

    # Checks above
    if l > 0:
        for x in range(len(num) + 2):
            check = index-1+x
            if (check >= 0) and (check < len(engine[l-1])) and (engine[l-1][check] != '.') and (not engine[l-1][check].isnumeric()):
                return int(num)

    # Checks below
    if l < len(engine)-1:
        for x in range(len(num) + 2):
            check = index-1+x
            if (check >= 0) and (check < len(engine[l+1])) and (engine[l+1][check] != '.') and (not engine[l+1][check].isnumeric()):
                return int(num)

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
                ans += checkNeighbours(l, startIndex, num)
                num = ""
            continue

        if not counting:
            startIndex = index

            counting = True
        num += value

        if index == len(engine[l])-1:
            counting = False
            ans += checkNeighbours(l, startIndex, num)
            num = ""

print(ans)
