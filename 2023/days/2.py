import utils.read_file as utils

def main():
    games = utils.read_file(2)

    part1 = part_one(games)
    part2 = part_two(games)

    print(f'Part 1: {part1} \nPart 2: {part2}')

def part_one(games):
    cap = {
        'red': 12,
        'green': 13,
        'blue': 14
    }

    pos_games = set()
    imp_games = set()

    for game in games:
        game_id, final = split_game(game)
        pos_games.add(int(game_id))

        for pull in final:
            for n, c in pull:
                if int(n) > cap[c]:
                    imp_games.add(int(game_id))

    final_games = pos_games - imp_games
    return sum(final_games)

def part_two(games):
    part2 = 0
    for game in games:

        cap = {
            'red': 0,
            'green': 0,
            'blue': 0
        }

        game_id, final = split_game(game)

        for pull in final:
            for n, c in pull:
                cap[c] = max(int(n), cap[c])

        part2 += (cap['red'] * cap['blue'] * cap['green'])

    return part2

def split_game(game):
    g, cubes = game.split(': ')

    _, game_id = g.split(' ')

    cs = cubes.split('; ')
    split_colours = [s.split(', ') for s in cs]

    final = [[n.split(' ') for n in pull] for pull in split_colours]

    return game_id, final

if __name__ == '__main__':
    main()