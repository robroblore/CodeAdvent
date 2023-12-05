f = open("input.txt", "r")

s = 0


for game in f:
    HIGHEST = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    power = 1
    game = game.strip()
    game = game.split(": ")
    id = int(game[0].split(" ")[1])
    game.pop(0)
    for match in game:
        match = match.split("; ")
        for round in match:
            round = round.split(", ")
            for play in round:
                play = play.split(" ")
                if int(play[0]) > HIGHEST[play[1]]:
                    HIGHEST[play[1]] = int(play[0])

    print(id, HIGHEST)
    for value in HIGHEST.values():
        power *= value
    print(power)
    s += power


print(s)
