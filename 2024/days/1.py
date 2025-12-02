import utils.read_file as utils

def main():
    orig_location_ids = utils.read_file(1)
    
    left_list = []
    right_list = []
    for item in orig_location_ids:
        left, right = item.split('   ')
        left_list.append(int(left))
        right_list.append(int(right))
    
    s = part_one(left_list, right_list)
    t = part_two(left_list, right_list)

    print(f'Part 1: {s} \nPart 2: {t}')


def part_one(left_list, right_list):
    left_list.sort()
    right_list.sort()
    diff_list = [abs(left_list[i] - right_list[i]) for i in range(len(left_list))]
    return sum(diff_list)

def part_two(left_list, right_list):
    count_list = []
    for l in left_list:
        right_count = right_list.count(l)
        count_list.append(right_count * l)

    return sum(count_list)

if __name__ == '__main__':
    main()