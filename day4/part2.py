import time

def count_cards(cards):
    global ans

    for card in cards:
        ans += 1
        if card in new_cards:
            count_cards(new_cards[card])


f = open("input.txt", "r")

new_cards = {}
ans = 0

for card in f:
    card = card.strip()
    card = card.split(": ")
    card_id = int(card[0].split(" ")[1])
    ans += 1
    card.pop(0)

    card = card[0].split(" | ")
    winning_nums = card[0].split(" ")
    nums = card[1].split(" ")

    counter = 0

    for num in nums:
        if num in winning_nums:
            counter += 1

    if counter != 0:
        new_cards[card_id] = []
        for x in range(1, counter + 1):
            new_cards[card_id].append(card_id + x)

ans = 193
s = time.time()
# Chatgpt method
for x in new_cards:
    stack = [new_cards[x]]
    while stack:
        current_cards = stack.pop()
        ans += len(current_cards)
        for card in current_cards:
            if card in new_cards:
                stack.append(new_cards[card])
e = time.time()
print(f"ChatGPT's method found: {ans} in {e - s}s")

ans = 193
s = time.time()
# My method
for x in new_cards:
    count_cards(new_cards[x])
e = time.time()
print(f"My method found: {ans} in {e - s}s")


print(ans)
