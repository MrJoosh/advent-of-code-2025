"""
Python implementation of the solution for day 5 of Advent of Code 2025
"""

from collections import deque


def main(input_file_name: str) -> int:
    with open(input_file_name, "r", encoding="utf-8") as input_file:
        input_data: list[str] = input_file.read().splitlines()

    fresh_ranges_raw: list[str] = input_data[: input_data.index("")]

    # Create a list of range objects from the provided range values
    fresh_ranges: list[tuple[int, int]] = []
    for r in fresh_ranges_raw:
        start, end = r.split("-")
        fresh_ranges.append((int(start), int(end)))
    fresh_ranges.sort()

    # Below logic thanks to /u/drz34257 on reddit - liked the solution so "borrowed" it.

    # Inspect and combine the ranges on a stack, pull out when not overlapping
    que_ranges: deque[tuple[int, int]] = deque(fresh_ranges)
    que_merged: deque[tuple[int, int]] = deque()

    while True:
        if len(que_ranges) == 1:
            # Last entry in the queue, so just add it on and finish processing
            que_merged.append(que_ranges.popleft())
            break
        a_min, a_max = que_ranges.popleft()
        b_min, b_max = que_ranges.popleft()

        if b_min > a_max:
            # Ranges don't overlap, so add the a range to the merged, and put b back on the stack
            que_merged.append((a_min, a_max))
            que_ranges.appendleft((b_min, b_max))
        else:
            # Ranges overlap, so add a range that combines both
            que_ranges.appendleft((a_min, max(a_max, b_max)))

    num_fresh_ids: int = 0
    while que_merged:
        # Loop through the merged ranges and sum the available values
        min_id, max_id = que_merged.popleft()
        num_fresh_ids += max_id - min_id + 1

    return num_fresh_ids


if __name__ == "__main__":
    print("### Test ###")
    result = main("test.txt")
    print(f"Result: {result} ({'Pass' if result == 14 else 'Fail'})")
    print("### Main ###")
    print(f"Result: {main('input.txt')}")
