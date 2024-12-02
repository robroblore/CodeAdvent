f = open("input.txt", "r")

c = 0

for l in f.readlines():
    lvls = list(map(int, l.strip().split()))

    isSafe = True

    isAsc = lvls[0] < lvls[1]

    for i in range(len(lvls)-1):
        if lvls[i] > lvls[i+1] and isAsc:
            isSafe = False
            break

        if lvls[i] < lvls[i+1] and not isAsc:
            isSafe = False
            break

        if abs(lvls[i] - lvls[i+1]) < 1 or abs(lvls[i] - lvls[i+1]) > 3:
            isSafe = False
            break

    print(lvls, isSafe)

    c += 1 if isSafe else 0

print(c)