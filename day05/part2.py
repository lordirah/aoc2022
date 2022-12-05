from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> str:
    lines = s.splitlines()
    data_dict = dict()
    final = ''
    for line in lines:
        if line.startswith(' 1'):
            keys_pos = list(line)
    for pos, key in enumerate(keys_pos):
        if key != ' ':
            data_dict[key] = []
            for line in lines:
                if line.startswith(' 1'):
                    break
                if list(line)[pos] != ' ':
                    data_dict[key].insert(0, list(line)[pos])
    for i, line in enumerate(lines):
        if line == '':
            empty_line = i
    for i, line in enumerate(lines):
        if i > empty_line:
            row = line.split(' ')
            no_items = row[1]
            key = row[3]
            to_key = row[5]
            temp_lst = []
            for i in range(int(no_items)):
                temp_lst.append(data_dict[key].pop(-1))
            temp_lst.reverse()
            for items in temp_lst:
                data_dict[to_key].append(items)
    for k, v in data_dict.items():
        final = final + v[-1]
    return final


INPUT_S = '''\
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
'''
EXPECTED = 'MCD'


@pytest.mark.parametrize(
    ('input_s', 'expected'),
    (
        (INPUT_S, EXPECTED),
    ),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('data_file', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file) as f, support.timing():
        print(compute(f.read()))

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
