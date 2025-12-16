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

    removed_rolls: int = 0
    while True:
        accessible_rolls, paper_roll_map = get_accessible_rolls(paper_roll_map)

        removed_rolls += accessible_rolls

        if accessible_rolls == 0:
            break

    return removed_rolls


def get_accessible_rolls(
    paper_roll_map: list[list[str]],
) -> tuple[int, list[list[str]]]:
    """
    Function to calculate a count of accessible rolls and return the map with the rolls removed.
    """

    accessible_rolls: int = 0

    for y, row in enumerate(paper_roll_map):
        for x, col in enumerate(row):
            if col != "@":
                continue
            num_neighbours = 0
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
                paper_roll_map[y][x] = "x"

    return accessible_rolls, paper_roll_map


if __name__ == "__main__":
    print("### Test ###")
    result = main("test.txt")
    print(f"Result: {result} ({'Pass' if result == 43 else 'Fail'})")
    print("### Main ###")
    print(f"Result: {main('input.txt')}")
