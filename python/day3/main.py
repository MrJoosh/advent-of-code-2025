"""
Python implementation of the solution for day 3 of Advent of Code 2025
"""


def main(input_file_name: str) -> int:
    with open(input_file_name, "r", encoding="utf-8") as input_file:
        banks = input_file.read().splitlines()

    bank_joltages: list[int] = []
    for bank in banks:
        possible_joltages: list[int] = []
        for i, left in enumerate(bank):
            for right in bank[i + 1 :]:
                possible_joltages.append(int(f"{left}{right}"))
        bank_joltages.append(max(possible_joltages))
    return sum(bank_joltages)


if __name__ == "__main__":
    print("### Test ###")
    result = main("test.txt")
    print(f"Result: {result} ({'Pass' if result == 357 else 'Fail'})")
    print("### Main ###")
    print(f"Result: {main('input.txt')}")
