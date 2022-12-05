from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    lines = s.splitlines()
    counter = 0
    for line in lines:
        range_pair = line.split(',')
        pair_1_start_value = int(range_pair[0].split('-')[0])
        pair_1_end_value = int(range_pair[0].split('-')[1])
        pair_2_start_value = int(range_pair[1].split('-')[0])
        pair_2_end_value = int(range_pair[1].split('-')[1])
        set_1 = set()
        set_2 = set()
        for i in range(pair_1_start_value, pair_1_end_value + 1):
            set_1.add(i)
        for i in range(pair_2_start_value, pair_2_end_value + 1):
            set_2.add(i)
        a_b = set_1.intersection(set_2)
        if len(a_b) > 0:
            counter += 1
    return counter


INPUT_S = '''\
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
'''
EXPECTED = 4


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
