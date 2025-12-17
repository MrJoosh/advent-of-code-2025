"""
Python implementation of the solution for day 6 of Advent of Code 2025
"""

import math


def main(input_file_name: str) -> int:
    with open(input_file_name, "r", encoding="utf-8") as input_file:
        input_data_raw: list[str] = input_file.read().splitlines()
    # Split the data into columns by whitespace
    input_data: list[list[str]] = [line.split() for line in input_data_raw]

    # Transpose the data into columnar lists
    input_columnar: list[list[str]] = list(map(list, zip(*input_data)))

    problem_results: list[int] = []
    for problem in input_columnar:
        operand = problem.pop()
        problem_results.append(calculate_problem(operand, *problem))

    return sum(problem_results)


def calculate_problem(operand: str, *values: str) -> int:
    """
    Helper function to calculate the result of the function arguments calculated with the given operand
    """
    # Convert str input to ints
    int_values = [int(val) for val in values]

    # Solve the problem
    match operand:
        case "+":
            return sum(int_values)
        case "*":
            return math.prod(int_values)
        case _:
            raise NotImplementedError(f"Unexpected operand '{operand}'")


if __name__ == "__main__":
    print("### Test ###")
    result = main("test.txt")
    print(f"Result: {result} ({'Pass' if result == 4277556 else 'Fail'})")
    print("### Main ###")
    print(f"Result: {main('input.txt')}")
