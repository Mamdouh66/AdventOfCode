def solution():
    with open("puz_in.txt", "r") as f:
        text = f.readlines()
        to_sum = []
        counter = 0
        for card in text:
            card = card[7:]
            winning_nums, checking_nums = card.split("|")
            checking_nums = checking_nums.split()
            winning_nums = winning_nums.split()
            for number in checking_nums:
                if number in winning_nums:
                    if counter == 0:
                        counter = 1
                    else:
                        counter *= 2
            to_sum.append(counter)
            counter = 0
        return sum(to_sum)


sol = solution()
print((sol, sol == 21821))
