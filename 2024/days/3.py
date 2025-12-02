import re

import utils.read_file as utils

def main():
    input_vals = utils.read_file(3)
    # please()
    # input_vals = ["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"]
    s = part_one(input_vals)
    t = part_two(input_vals)

    print(f'Part 1: {s} \nPart 2: {t}')

def part_one(corrupted):
    mul = r'mul\(\d+,\d+\)'
    digits = r'\d+'
    multiplied = []
    for line in corrupted:
        mully = re.findall(mul, line)
        for i in mully:
            a, b = re.findall(digits, i)
            multiplied.append(int(a) * int(b))
            
    return sum(multiplied)
  
def part_two(corrupted):
    corrupted = [''.join(corrupted)]
    do_mul = []
    for line in corrupted:
        dos = line.split('do()')
        for d in dos:
            parted = d.split("don't()")
            do_mul.append(parted[0])
    
    return part_one(do_mul)

if __name__ == '__main__':
    main()