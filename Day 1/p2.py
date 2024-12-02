f = open("input2.txt", "r")

ls = []

rs = {}

for x in f.readlines():
    l, r = map(int, x.strip().split("   "))
    ls.append(l)

    if r not in rs:
        rs[r] = 1
    else:
        rs[r] += 1

s = 0

for x in ls:
    if x in rs:
        s += x * rs[x]

print(s)