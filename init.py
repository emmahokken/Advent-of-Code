import os

def main():
    year = input('What year is it? ')
    os.mkdir(year)
    os.mkdir(f'{year}/days')
    os.mkdir(f'{year}/input')
    os.mkdir(f'{year}/output')
    print('Done! Have fun!')

if __name__ == '__main__':
    main()