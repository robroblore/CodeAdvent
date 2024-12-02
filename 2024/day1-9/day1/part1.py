# This one was done on a separate machine and I won't bother to do it again :)
f = open("input.txt", "r")
l, r = [], []
for x in f.readlines():
    x = x.rstrip().split("   ")
    l.append(int(x[0]))
    r.append(int(x[1]))

l.sort()
r.sort()
s = 0
for i in range(len(l)):
    s += abs(l[i] - r[i])

print(s)
