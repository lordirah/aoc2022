from __future__ import annotations

import argparse
import os.path
from collections import defaultdict
import pytest
import support

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')


def compute(s: str) -> int:
    SZ = defaultdict(int)
    path = []
    lines = s.splitlines()
    for line in lines:
        words = line.strip().split()
        if words[1] == 'cd':
            if words[2] == '..':
                path.pop()
            else:
                path.append(words[2])
        elif words[1] == 'ls':
            continue
        elif words[0] == 'dir':
            continue
        else:
            sz = int(words[0])
            # Add this file's size to the current directory size *and* the size of all parents
            for i in range(1, len(path)+1):
                SZ['/'.join(path[:i])] += sz

    max_used = 70000000 - 30000000
    total_used = SZ['/']
    need_to_free = total_used - max_used

    p1 = 0
    p2 = 1e9
    for k, v in SZ.items():
        # print(k,v)
        if v <= 100000:
            p1 += v
        if v >= need_to_free:
            p2 = min(p2, v)
    print(p1)
    print(p2)


INPUT_S = '''\
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
'''
EXPECTED = 95437


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
