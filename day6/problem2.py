def solution():
    with open("puz_in.txt", "r") as f:
        text = f.readlines()
        times = "".join(text[0].split(":")[1].strip().split())
        distances = "".join(text[1].split(":")[1].strip().split())
        counter = 0
        counter_mul = 1
        for i in range(1, int(times) + 1):
            if (int(times) - int(i)) * int(i) > int(distances):
                counter += 1
            counter_mul *= counter
        # for i in range(int(times) + 1):
        #     for j in range(1, int(i) + 1):
        #         if ((int(i) - int(j)) * int(j)) > int(distances[i]):
        #             counter += 1
        return counter


print(solution())
