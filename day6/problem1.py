def solution():
    with open("puz_in.txt", "r") as f:
        text = f.readlines()
        times = text[0].split(":")[1].strip().split()
        distances = text[1].split(":")[1].strip().split()
        counter = 0
        counter_mul = 1
        for idx, i in enumerate(times):
            for j in range(1, int(i) + 1):
                if ((int(i) - int(j)) * int(j)) > int(distances[idx]):
                    counter += 1
            counter_mul *= counter
            counter = 0
        return counter_mul


print(solution())
