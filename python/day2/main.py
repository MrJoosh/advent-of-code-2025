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
            id_pattern: str = ""
            repeat: bool = True
            for c in str(id):
                if id_pattern.startswith(c):
                    num_patterns = len(str(id)) // len(id_pattern)
                    if str(id) == id_pattern * num_patterns:
                        # Pattern repeating
                        repeat = True
                        break
                id_pattern += c
                if len(id_pattern) > len(str(id)) // 2:
                    # If pattern is longer than half the length of the id, it can't repeat so bail.
                    repeat = False
                    break
            if not repeat:
                continue

            # At this point we can be confident that this id is a repeating pattern
            invalid_ids.append(id)

    return sum(invalid_ids)


if __name__ == "__main__":
    # Run test:
    print("### Test ###")
    test_result = main("test.txt")
    print(f"Result: {test_result} ({'pass' if test_result == 4174379265 else 'fail'})")
    print("### Main ###")
    print(f"Result: {main('input.txt')}")
