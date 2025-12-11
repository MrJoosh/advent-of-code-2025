"""
Python implementation of the solution for day 2 of Advent of Code 2025
"""


def main(input_file_path: str) -> int:
    with open(input_file_path, "r", encoding="utf-8") as input_file:
        id_ranges = input_file.read().replace("\n", "").split(",")

    # Invalid IDs have repeating patterns
    invalid_ids: list[int] = []
    for id_range in id_ranges:
        for id in range(int(id_range.split("-")[0]), int(id_range.split("-")[1]) + 1):
            if str(id)[: len(str(id)) // 2] == str(id)[len(str(id)) // 2 :]:
                invalid_ids.append(id)

    print(invalid_ids)

    return sum(invalid_ids)


if __name__ == "__main__":
    print(f"Result: {main('input.txt')}")
