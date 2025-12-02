import utils.read_file as utils

def main():
    input_vals = utils.read_file(1)
    input_test_vals = utils.read_test_file(1)

    s = part_one(input_vals)
    t = part_two(input_vals)

    print(f'Part 1: {s} \nPart 2: {t}')

def part_one(input_vals: list[str]):
    i = 50
    visits = 0

    lr_split = [(s[0].upper(), int(s[1:])) for s in input_vals]
    for direction, steps in lr_split:
        if direction == 'L':
            i = (i - steps) % 100
        elif direction == 'R':
            i = (i + steps) % 100

        if i == 0:
            visits += 1
            
    return visits

def part_two(input_vals: list[str]):
    i = 50
    visits = 0

    lr_split = [(s[0].upper(), int(s[1:])) for s in input_vals]   
    for direction, steps in lr_split:
        if direction == 'L':
            prev_i = i
            i = (i - steps) % 100
            if prev_i > 0 and prev_i < i:
                visits += 1
            elif i == 0:
                visits += 1
            if steps >= 100:
                visits += steps // 100

        elif direction == 'R':
            prev_i = i
            i = (i + steps) % 100
            if prev_i > 0 and prev_i > i:
                visits += 1
            elif i == 0:
                visits += 1
            if steps >= 100:
                visits += steps // 100

    return visits

if __name__ == '__main__':
    main()