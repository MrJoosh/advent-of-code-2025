"""
Python implementation of the solution for day 5 of Advent of Code 2025
"""


def main(input_file_name: str) -> int:
    with open(input_file_name, "r", encoding="utf-8") as input_file:
        input_data: list[str] = input_file.read().splitlines()

    fresh_ranges_raw: list[str] = input_data[: input_data.index("")]
    ids: list[str] = input_data[input_data.index("") + 1 :]

    # Create a list of range objects from the provided range values
    fresh_ranges: list[range] = [
        range(int(r[: r.find("-")]), int(r[r.find("-") + 1 :]) + 1)
        for r in fresh_ranges_raw
    ]

    fresh_id_count: int = 0
    fresh_ids: list[int] = []
    for id in ids:
        for fresh_range in fresh_ranges:
            if int(id) in fresh_range:
                fresh_id_count += 1
                fresh_ids.append(int(id))
                break
    # print(fresh_ids)
    return fresh_id_count


if __name__ == "__main__":
    print("### Test ###")
    result = main("test.txt")
    print(f"Result: {result} ({'Pass' if result == 3 else 'Fail'})")
    print("### Main ###")
    print(f"Result: {main('input.txt')}")
