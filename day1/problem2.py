def solution():
    words = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    with open("input.txt", "r") as f:
        text = f.read().splitlines()
        nums = list()
        for line in text:
            digits = str()
            letters = str()
            for letter in line:
                letters += letter
                if letter.isdigit():
                    digits += letter
                else:
                    for word in words:
                        if word in letters:
                            digits += str(words[word])
                            letters = letter
                            break
            if digits:
                nums.append(int(f"{digits[0]}{digits[-1]}"))
        return sum(nums)


print(solution())
