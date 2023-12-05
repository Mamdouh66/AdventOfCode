def solution():
    with open("puz_in.txt", "r") as f:
        text = f.readlines()
        cards = {key: 1 for key in range(len(text))}
        counter = 0
        for index, card in enumerate(text):
            card = card[7:]
            winning_nums, checking_nums = card.split("|")
            checking_nums = checking_nums.split()
            winning_nums = winning_nums.split()
            for number in checking_nums:
                if number in winning_nums:
                    counter += 1
            for temp_index in range(1, counter + 1):
                for _ in range(cards[index]):
                    cards[index + temp_index] += 1
            counter = 0
        return sum(cards.values())


sol = solution()
print((sol, sol == 5539496))
