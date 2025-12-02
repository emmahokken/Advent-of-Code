import utils.read_file as utils

def main():
    orig_cal_vals = utils.read_file(1)

    s = part_one(orig_cal_vals)
    t = part_two(orig_cal_vals)

    print(f'Part 1: {s} \nPart 2: {t}')

def part_one(orig_cal_vals):
    s = 0
    for ocv in orig_cal_vals:
        cv = [i for i in ocv if i.isdigit()]
        s += int(cv[0] + cv[-1])

    return s

def part_two(orig_cal_vals):
    t = 0

    number_dict = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        'zero': '0',
    }


    for ocv in orig_cal_vals:
        digits = []
        for i, c in enumerate(ocv):
            if c.isdigit():
                digits.append(c)
            else:
                for key in number_dict.keys():
                    if ocv[i:].startswith(key):
                        digits.append(number_dict[key])

        print(digits)
        t += int(digits[0] + digits[-1])

    return t

def part2():
    values = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

    pairs = []
    for line in input:
        digits = []
        # start at the first letter and move through it letter by letter.
        # this is the only way i've found to account for overlapping words.
        # an example is "oneight", which only matches "one" when using re.findall.
        for i,c in enumerate(line):
            if line[i].isdigit():
                digits.append(line[i])
            else:
                for k in values.keys():
                    if line[i:].startswith(k):
                        digits.append(values[k])
                        pairs.append(int(f"{digits[0]}{digits[-1]}"))

if __name__ == '__main__':
    main()
