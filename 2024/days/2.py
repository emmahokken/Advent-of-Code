import utils.read_file as utils

def main():
    reports = utils.read_file(2)
    split_reports = [[int(x) for x in line.split(' ')] for line in reports]

    s = part_one(split_reports)
    t = part_two(split_reports)

    print(f'Part 1: {s} \nPart 2: {s+t}')

def part_one(reports):
    '''
    Reports are safe if:
    - increasing or decreasing
    - difference between number is 1-3
    '''
    safe = 0 
    for report in reports:
       if check_safe(report):
            safe += 1
    
    return safe

def part_two(reports):
    safe = 0 
    for i, report in enumerate(reports):
       if not check_safe(report):
            for i in range(len(report)):
                prob_case = report[:]
                prob_case.pop(i)
                if check_safe(prob_case):
                    safe += 1
                    break

    return safe
    
    
def check_safe(report):
    increasing = all(i < j for i, j in zip(report, report[1:]))
    decreasing = all(i > j for i, j in zip(report, report[1:]))
    small_diff = all(abs(r - report[i+1]) < 4 for i, r in enumerate(report[:-1]))

    if (increasing or decreasing) and small_diff:
        return True
    return False 

if __name__ == '__main__':
    main()