def parse_inputs(inputs):
    inputs = list(map(int, inputs.split(":")[1].split()))
    seeds = []
    for i in range(0, len(inputs), 2):
        seeds.append((inputs[i], inputs[i] + inputs[i + 1]))
    return seeds


def parse_block(block):
    ranges = []
    for line in block.splitlines()[1:]:
        ranges.append(list(map(int, line.split())))
    return ranges


def process_seeds(seeds, ranges):
    new_seeds = []
    while len(seeds) > 0:
        start, end = seeds.pop()
        for range_start, range_end, range_length in ranges:
            overlap_start = max(start, range_end)
            overlap_end = min(end, range_end + range_length)
            if overlap_start < overlap_end:
                new_seeds.append(
                    (
                        overlap_start - range_end + range_start,
                        overlap_end - range_end + range_start,
                    )
                )
                if overlap_start > start:
                    seeds.append((start, overlap_start))
                if end > overlap_end:
                    seeds.append((overlap_end, end))
                break
        else:
            new_seeds.append((start, end))
    return new_seeds


def solution():
    with open("puz_in.txt", "r") as file:
        inputs, *blocks = file.read().split("\n\n")
        seeds = parse_inputs(inputs)

        for block in blocks:
            ranges = parse_block(block)
            seeds = process_seeds(seeds, ranges)

        return min(seeds)[0]


print(solution() == 15290096)
