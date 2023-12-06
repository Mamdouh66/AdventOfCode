def parse_seeds(seeds):
    return list(map(int, seeds.split(":")[1].split()))


def parse_block(block):
    ranges = []
    for line in block.splitlines()[1:]:
        ranges.append(list(map(int, line.split())))
    return ranges


def process_seeds(seeds, ranges):
    new_seeds = []
    for seed in seeds:
        for range_start, range_end, range_length in ranges:
            if range_end <= seed < range_end + range_length:
                new_seeds.append(seed - range_end + range_start)
                break
        else:
            new_seeds.append(seed)
    return new_seeds


def solution():
    with open("puz_in.txt", "r") as file:
        seeds, *blocks = file.read().split("\n\n")
        seeds = parse_seeds(seeds)

        for block in blocks:
            ranges = parse_block(block)
            seeds = process_seeds(seeds, ranges)

        return min(seeds)


print(solution())
