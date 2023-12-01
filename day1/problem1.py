def solution():
    with open("input.txt", "r") as f:
        text = f.read().splitlines()
        nums = list()
        for line in text:
            digits = str()
            for letter in line:
                if letter.isdigit():
                    digits += letter
            if digits:
                nums.append(int(f"{digits[0]}{digits[-1]}"))
    return sum(nums)


print(solution())
