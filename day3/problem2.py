def out_of_bound(row, col, text):
    return not (
        row < 0
        or row >= len(text)
        or col < 0
        or col >= len(text[row])
        or text[row][col].isdigit()
    )


def get_number_point(row, col, text):
    for i in range(col, -1, -1):
        if i == 0 or not text[row][i - 1].isdigit():
            col = i
            break
    return (row, col)


def solution():
    with open("day3/puz_in.txt", "r") as f:
        text = f.readlines()
        ans = 0
        for row, line in enumerate(text):
            for col, ch in enumerate(line):
                if ch == "*":
                    points = set()

                    for row_i in range(row - 1, row + 2):
                        for col_i in range(col - 1, col + 2):
                            if not out_of_bound(row_i, col_i, text):
                                points.add(get_number_point(row_i, col_i, text))

                    if len(points) == 2:
                        to_sum = []
                        for row_p, col_p in points:
                            number = ""
                            for ch in text[row_p][col_p:]:
                                if ch.isdigit():
                                    number += ch
                                else:
                                    break
                            to_sum.append(int(number))
                        ans += to_sum[0] * to_sum[1]
        return ans


sol = solution()
print(f"Value: {sol} and it's {sol == 467835}")
