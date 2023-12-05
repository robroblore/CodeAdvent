f = open("input.txt", "r")

ans = 0
for card in f:
    card = card.strip()
    card = card.split(": ")
    id = int(card[0].split(" ")[1])
    card.pop(0)

    card = card[0].split(" | ")
    winning_nums = card[0].split(" ")
    nums = card[1].split(" ")

    counter = 0
    value = 0

    for num in nums:
        if num in winning_nums:
            counter += 1

    if counter == 1:
        value = 1
    elif counter > 1:
        value = 2 ** (counter-1)

    ans += value

print(ans)