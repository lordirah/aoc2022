from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    win_list = [
        ['A', 'Y'],
        ['B', 'Z'],
        ['C', 'X']
    ]
    lose_list = [
        ['A', 'Z'],
        ['B', 'X'],
        ['C', 'Y']
    ]
    total_score = 0
    win_score = 6
    score_dict = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }
    lines = s.splitlines()
    for line in lines:
        turn_lst = line.split(' ')
        if turn_lst in win_list:
            total_score = total_score + score_dict[turn_lst[1]] + win_score
        elif turn_lst in lose_list:
            total_score = total_score + score_dict[turn_lst[1]]
        else:
            total_score = total_score + score_dict[turn_lst[1]] + 3
    return total_score


INPUT_S = '''\
A Y
B X
C Z
'''
EXPECTED = 15


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
