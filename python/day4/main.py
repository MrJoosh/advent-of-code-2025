"""
Python implementation of the solution for day 4 of Advent of Code 2025
"""

"""
(-1,-1) ( 0,-1) ( 1,-1)
(-1, 0) ( 0, 0) ( 1, 0)
(-1, 1) ( 0, 1) ( 1, 1)

"""


def main(input_file_name: str) -> int:
    # First read the input into a 2d array
    with open(input_file_name, "r", encoding="utf-8") as input_file:
        paper_roll_map: list[list[str]] = [
            list(row) for row in input_file.read().splitlines()
        ]

    accessible_rolls: int = 0

    for y, row in enumerate(paper_roll_map):
        for x, col in enumerate(row):
            if col != "@":
                continue
            num_neighbours = 0
            # Check row above (-y)
            for ry in range(-1, 2):
                test_y = y + ry
                if test_y < 0 or test_y > len(paper_roll_map) - 1:
                    continue
                for rx in range(-1, 2):
                    test_x = x + rx
                    if test_x < 0 or test_x > len(row) - 1:
                        continue
                    if ry == rx == 0:
                        continue
                    num_neighbours += 1 if paper_roll_map[y + ry][x + rx] == "@" else 0
            if num_neighbours < 4:
                accessible_rolls += 1

    return accessible_rolls


if __name__ == "__main__":
    print("### Test ###")
    result = main("test.txt")
    print(f"Result: {result} ({'Pass' if result == 13 else 'Fail'})")
    print("### Main ###")
    print(f"Result: {main('input.txt')}")
