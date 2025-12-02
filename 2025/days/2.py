import utils.read_file as utils

def main():
    input_vals = utils.read_file_comma_separated(2)
    input_test_vals = utils.read_test_file_comma_separated(2)
    
    s = part_one(input_vals)
    t = part_two(input_vals)

    print(f'Part 1: {s} \nPart 2: {t}')

def part_one(input_vals):
    total = 0
    for prod_range in input_vals:
        start, end = prod_range.split('-')

        # iterate through each number in the range
        for item_id in range(int(start), int(end) + 1):
            s = str(item_id)
            # check if the number has an even number of digits
            if len(s) >= 2 and len(s) % 2 == 0:
                # split the number in half
                mid = len(s) // 2  
                left, right = int(s[:mid]), int(s[mid:])
                # compare the two halves
                if left == right:
                    total += item_id

    return total


def part_two(input_vals):
    total = 0
    for prod_range in input_vals:
        start, end = prod_range.split('-')

        # iterate through each number in the range
        for item_id in range(int(start), int(end) + 1):
            s = str(item_id)

            # check for any repeated sequence
            for n in range(len(s), 1, -1):
                # only consider lengths that divide evenly
                if len(s) % n != 0:
                    continue

                # split the string into n equal parts
                chunk_size = len(s) // n
                parts = [s[i:i + chunk_size] for i in range(0, len(s), chunk_size)]

                # check if all parts are the same
                if all(p == parts[0] for p in parts):
                    total += item_id
                    break

    return total

if __name__ == '__main__':
    main()