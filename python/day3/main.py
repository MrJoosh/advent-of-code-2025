"""
Python implementation of the solution for day 3 of Advent of Code 2025
"""


def main(input_file_name: str) -> int:
    with open(input_file_name, "r", encoding="utf-8") as input_file:
        banks = input_file.read().splitlines()

    bank_joltages: list[int] = []
    for bank in banks:
        # Find the first digit of the max joltage
        max_batt, idx = find_max_in_bank(bank[: ((len(bank) - 12) + 1)])
        bank_joltage = str(max_batt)
        # Find the rest of the digits of the max joltage from the remaining digits
        for digits_left in range(11, 0, -1):
            idx += 1
            if digits_left == len(bank[idx:]):
                bank_joltage += bank[idx:]
                break
            next_best, offset = find_max_in_bank(
                bank[idx : (idx + ((len(bank[idx:]) - digits_left) + 1))]
            )
            idx += offset
            bank_joltage += str(next_best)
        bank_joltages.append(int(bank_joltage))

    return sum(bank_joltages)


def find_max_in_bank(bank: str) -> tuple[int, int]:
    max_value: int = -1
    max_index: int = 0

    for idx, batt in enumerate(bank):
        if int(batt) > max_value:
            max_value = int(batt)
            max_index = idx
    return max_value, max_index


if __name__ == "__main__":
    print("### Test ###")
    result = main("test.txt")
    print(f"Result: {result} ({'Pass' if result == 3121910778619 else 'Fail'})")
    print("### Main ###")
    print(f"Result: {main('input.txt')}")
