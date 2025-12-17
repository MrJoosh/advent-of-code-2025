#!/bin/zsh

DAY_NUMBER=$1

PYTHON_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &>/dev/null && pwd)

DIR_NAME=day${DAY_NUMBER}

mkdir ${DIR_NAME}

pushd ${DIR_NAME}

touch input.txt puzzle.md test.txt

cat >main.py <<EOL
"""
Python implementation of the solution for day ${DAY_NUMBER} of Advent of Code 2025
"""

def main(input_file_name: str) -> int:
    with open(input_file_name, "r", encoding="utf-8") as input_file:
        input_data_raw: list[str] = input_file.read().splitlines()
    return 0


if __name__ == "__main__":
    print("### Test ###")
    result = main("test.txt")
    print(f"Result: {result} ({'Pass' if result == 999 else 'Fail'})")
    print("### Main ###")
    print(f"Result: {main('input.txt')}")

EOL

popd &>/dev/null

exit 0
