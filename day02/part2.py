from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    win_dict = {
        'A': 'B',
        'B': 'C',
        'C': 'A'
    }
    lose_dict = {
        'A': 'C',
        'B': 'A',
        'C': 'B'
    }
    score_dict = {
        'A': 1,
        'B': 2,
        'C': 3
    }
    lines = s.splitlines()
    total_score = 0
    for line in lines:
        turn_lst = line.split(' ')
        if turn_lst[1] == 'Y':
            total_score = total_score + score_dict[turn_lst[0]] + 3
        elif turn_lst[1] == 'X':
            total_score = total_score + score_dict[lose_dict[turn_lst[0]]]
        else:
            total_score = total_score + score_dict[win_dict[turn_lst[0]]] + 6
    return total_score


INPUT_S = '''\
A Y
B X
C Z
'''
EXPECTED = 12


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
