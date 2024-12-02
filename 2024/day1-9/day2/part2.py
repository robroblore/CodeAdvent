f = open("input.txt", "r")

c = 0

for l in f.readlines():
    lvls = list(map(int, l.strip().split()))
    print(lvls, end=" ")
    lvlscopy = lvls.copy()

    isSafe = [True, True]

    isAsc = lvls[0] < lvls[1]

    possLvls = []

    for i in range(len(lvls) - 1):
        if lvls[i] > lvls[i + 1] and isAsc:
            lvlscopy.remove(lvls[i + 1])
            possLvls.append(lvlscopy)
            lvls.remove(lvls[i])
            possLvls.append(lvls)
            break

        if lvls[i] < lvls[i + 1] and not isAsc:
            lvlscopy.remove(lvls[i + 1])
            possLvls.append(lvlscopy)
            lvls.remove(lvls[i])
            possLvls.append(lvls)
            break

        if abs(lvls[i] - lvls[i + 1]) < 1 or abs(lvls[i] - lvls[i + 1]) > 3:
            lvlscopy.remove(lvls[i + 1])
            possLvls.append(lvlscopy)
            lvls.remove(lvls[i])
            possLvls.append(lvls)
            break

    for l in range(len(possLvls)):
        lvls = possLvls[l]

        isAsc = lvls[0] < lvls[1]
        for i in range(len(lvls) - 1):
            if lvls[i] > lvls[i + 1] and isAsc:
                isSafe[l] = False
                break

            if lvls[i] < lvls[i + 1] and not isAsc:
                isSafe[l] = False
                break

            if abs(lvls[i] - lvls[i + 1]) < 1 or abs(lvls[i] - lvls[i + 1]) > 3:
                isSafe[l] = False
                break

    print(any(isSafe))

    c += 1 if any(isSafe) else 0

print(c)
