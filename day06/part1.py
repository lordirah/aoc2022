from __future__ import annotations

import argparse
import os.path

import pytest

import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    total_length = len(s)
    counter_dict = dict()
    sub_char_counter = 0
    for index, c in enumerate(s.strip()):
        temp_list = []
        sub_char_counter += 1
        if index + 4 > total_length:
            print("No match found")
            break
        temp_list.append(c)
        temp_list.append(s[index+1])
        temp_list.append(s[index+2])
        temp_list.append(s[index+3])
        if len(set(temp_list)) == 4:
            break
    return index+4


INPUT_S = '''\
nppdvjthqldpwncqszvftbrmjlhg
'''
EXPECTED = 1


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
