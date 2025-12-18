"""
Python implementation of the solution for day 7 of Advent of Code 2025
"""

from collections import Counter


def main(input_file_name: str) -> int:
    with open(input_file_name, "r", encoding="utf-8") as input_file:
        input_data_raw: list[str] = input_file.read().splitlines()

    # Part 2 solution by /u/mnvrth (https://github.com/mnvr/aoc-25/blob/main/07.py)
    paths: Counter = Counter()  # outner object of paths taken
    splits: int = 0  # Number of times the beam has split

    for line in input_data_raw:
        for i, c in enumerate(line):
            match c:
                case "S":
                    paths[i] = 1
                case "^":
                    if i in paths:
                        splits += 1
                        paths[i - 1] += paths[i]
                        paths[i + 1] += paths[i]
                        del paths[i]

    return paths.total()


if __name__ == "__main__":
    print("### Test ###")
    result = main("test.txt")
    print(f"Result: {result} ({'Pass' if result == 40 else 'Fail'})")
    print("### Main ###")
    print(f"Result: {main('input.txt')}")
