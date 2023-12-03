def solution():
    max_balls = {"red": 12, "green": 13, "blue": 14}
    with open("day2/puz_input.txt", "r") as f:
        games = f.read().splitlines()
        counter = 0
        for game in games:
            game_head, game_data = game.split(":")
            game_id = int(game_head.split()[1])
            turns = game_data.split(";")
            colors = {}
            for turn in turns:
                possible = True
                pairs = turn.split(",")
                for pair in pairs:
                    number, color = pair.split()
                    colors[color] = int(number)

                for ball in max_balls:
                    if ball in colors:
                        if colors[ball] > max_balls[ball]:
                            possible = False
                            break

                colors = {}
                if not possible:
                    break
            if possible:
                counter += game_id

        return counter


print(solution())
