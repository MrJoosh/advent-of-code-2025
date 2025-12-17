"""
Python implementation of the solution for day 7 of Advent of Code 2025
"""

from collections import deque


def main(input_file_name: str) -> int:
    with open(input_file_name, "r", encoding="utf-8") as input_file:
        input_data_raw: deque[str] = deque(input_file.read().splitlines())

    beams: list[int] = []  # List of indices that have a beam
    splits: int = 0  # Number of times the beam has split
    while True:
        try:
            row: str = input_data_raw.popleft()
        except IndexError:
            break
        if not beams:
            beams.append(row.find("S"))
            continue
        new_beams: list[int] = list(beams)
        for beam in beams:
            if row[beam] == "^":
                new_beams.remove(beam)
                new_beams.append(beam - 1)
                new_beams.append(beam + 1)
                splits += 1
        beams = list(set(new_beams))
    return splits


if __name__ == "__main__":
    print("### Test ###")
    result = main("test.txt")
    print(f"Result: {result} ({'Pass' if result == 21 else 'Fail'})")
    print("### Main ###")
    print(f"Result: {main('input.txt')}")
