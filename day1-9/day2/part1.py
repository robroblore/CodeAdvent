f = open("input.txt", "r")

MAX = {
    "red": 12,
    "green": 13,
    "blue": 14
}

s = 0


for game in f:
    impossible = False
    game = game.strip()
    game = game.split(": ")
    id = int(game[0].split(" ")[1])
    game.pop(0)
    for match in game:
        if impossible: break
        match = match.split("; ")
        for round in match:
            if impossible: break
            round = round.split(", ")
            for play in round:
                if impossible: break
                play = play.split(" ")
                if int(play[0]) > MAX[play[1]]:
                    impossible = True
    if not impossible:
        print(id, game)
        s += id

print(s)
