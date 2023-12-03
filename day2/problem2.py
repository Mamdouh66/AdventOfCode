def solution():
    with open("day2/puz_input.txt", "r") as f:
        games = f.read().splitlines()
        counter = 0
        for game in games:
            game_head, game_data = game.split(":")
            turns = game_data.split(";")
            colors = {"blue": 0, "red": 0, "green": 0}
            for turn in turns:
                pairs = turn.split(",")
                for pair in pairs:
                    number, color = pair.split()
                    if int(number) > colors[color]:
                        colors[color] = int(number)

            min_power = 1
            for color, value in colors.items():
                min_power *= value
            counter += min_power
            colors = {"blue": 0, "red": 0, "green": 0}

        return counter


print(solution() == 66016)
