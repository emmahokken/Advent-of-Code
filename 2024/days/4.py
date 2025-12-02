import numpy as np # type: ignore
import re

import utils.read_file as utils

def main():
    input_vals = utils.read_file(4)
    
    s = part_one(input_vals)
    t = part_two(input_vals)

    print(f'Part 1: {s} \nPart 2: {t}')

def part_one(wordsearch):
    ws = np.array([list(line) for line in wordsearch])
    x, y = ws.shape

    assert x == y

    occurances = 0
    xmas = 'XMAS'
    samx = 'SAMX'

    # horizontal and vertical
    for i in range(x):
        occurances += len(re.findall(xmas, ''.join(ws[i])))
        occurances += len(re.findall(samx, ''.join(ws[i])))
        occurances += len(re.findall(xmas, ''.join(ws[:, i])))
        occurances += len(re.findall(samx, ''.join(ws[:, i])))

    # diagonal
    aws = np.fliplr(ws)
    for i in range(-x, x):
        diag = np.diagonal(ws, i)
        adiag = np.diagonal(aws, i)

        occurances += len(re.findall(xmas, ''.join(diag)))
        occurances += len(re.findall(samx, ''.join(diag)))
        occurances += len(re.findall(xmas, ''.join(adiag)))
        occurances += len(re.findall(samx, ''.join(adiag)))

    return occurances

def part_two(wordsearch):
    ws = np.array([list(line) for line in wordsearch])
    x, y = ws.shape

    assert x == y

    occurances = 0
    M = 'M'
    A = 'A'
    S = 'S'

    for i in range(x-2):
        for j in range(y-2):
            a = ws[i,j]         # M
            b = ws[i,j+2]       # M
            c = ws[i+1, j+1]    # A
            d = ws[i+2, j]      # S 
            e = ws[i+2, j+2]    # S

            if a == M and b == M and c == A and d == S and e == S:
                occurances += 1
            if a == S and b == S and c == A and d == M and e == M:
                occurances += 1
            if a == M and b == S and c == A and d == M and e == S:
                occurances += 1
            if a == S and b == M and c == A and d == S and e == M:
                occurances += 1
    
    return occurances

if __name__ == '__main__':
    main()