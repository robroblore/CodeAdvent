f = open("input.txt", "r")
dic = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}
s = 0
for line in f:
    line = line.strip()
    numbers = []
    for key in dic:
        for index in range(len(line)):
            if line.startswith(key, index):
                numbers.append([index, dic[key]])

    for value in dic.values():
        for index in range(len(line)):
            if line.startswith(value, index):
                numbers.append([index, value])

    numbers.sort()
    print(int(numbers[0][1]) * 10 + int(numbers[-1][1]))
    s += int(numbers[0][1]) * 10 + int(numbers[-1][1])

print(s)
