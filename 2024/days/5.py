from itertools import permutations
from tqdm import tqdm # type: ignore

from functools import cmp_to_key

import utils.read_file as utils

def main():
    p, u = utils.read_file_double_whiteline(5)
    
    s, wrong_updates = part_one(p, u)
    t = part_two(p, wrong_updates)
    # print(stolen(p,u))
    print(f'Part 1: {s} \nPart 2: {t}')

def part_one(p, u):
    pors = [i.split('|') for i in p.split('\n')]
    updates = [i.split(',') for i in u.split('\n')]
    

    mid_values = 0
    wrong_updates = []
    for update in updates:
        wrong = False
        for before, after in pors:
            try:
                first = update.index(before)
                second = update.index(after)
                if first > second:
                    wrong = True
                    wrong_updates.append(update)
                    break
            except ValueError:
                continue

        if not wrong:
            # if we made it through, the updat is correct
            mid_values += int(update[len(update) // 2])

    return mid_values, wrong_updates

def my_cmp(a, b):
    pass

def part_two(p, wrong_updates):
    pors = [i.split('|') for i in p.split('\n')]
    mid_values = 0
    for update in wrong_updates:
        for before, after in pors:
            try:
                first = update.index(before)
                second = update.index(after)
                if first > second:
                    tmp = update[first]
                    update[first] = update[second]
                    update[second] = tmp                    
            except ValueError:
                continue
        for before, after in pors:
            try:
                first = update.index(before)
                second = update.index(after)
                if first > second:
                    tmp = update[first]
                    update[first] = update[second]
                    update[second] = tmp                    
            except ValueError:
                continue
        for before, after in pors:
            try:
                first = update.index(before)
                second = update.index(after)
                if first > second:
                    tmp = update[first]
                    update[first] = update[second]
                    update[second] = tmp                    
            except ValueError:
                continue
        for before, after in pors:
            try:
                first = update.index(before)
                second = update.index(after)
                if first > second:
                    tmp = update[first]
                    update[first] = update[second]
                    update[second] = tmp                    
            except ValueError:
                continue
        for before, after in pors:
            try:
                first = update.index(before)
                second = update.index(after)
                if first > second:
                    tmp = update[first]
                    update[first] = update[second]
                    update[second] = tmp                    
            except ValueError:
                continue
        for before, after in pors:
            try:
                first = update.index(before)
                second = update.index(after)
                if first > second:
                    tmp = update[first]
                    update[first] = update[second]
                    update[second] = tmp                    
            except ValueError:
                continue
        
        mid_values += int(update[len(update) // 2])
    return mid_values

    # for each rule
    # find index of value in update
    # if index a < index b
    #   switch

    pors = [i.split('|') for i in p.split('\n')]
    still_wrong = []

    mid_values = 0 
    for update in tqdm(wrong_updates):
        print(update)
        # reorder list
        possible_lists = permutations(update)
        for pl in possible_lists:
            wrong = False
            for before, after in pors:
                try:
                    first = pl.index(before)
                    second = pl.index(after)
                    if first > second:
                        wrong = True
                        break
                except ValueError:
                    continue

            if not wrong:
                # if we made it through, the updat is correct
                mid_values += int(pl[len(pl) // 2])
                print('fount it')
                break

    return mid_values

def stolen(rules, pages):
    cmp = cmp_to_key(lambda x, y: -(x+'|'+y in rules))
    
    a = [0, 0]
    for p in pages.split():
        p = p.split(',')
        s = sorted(p, key=cmp)
        a[p!=s] += int(s[len(s)//2])

    print(*a)

    print(4145)
if __name__ == '__main__':
    main()