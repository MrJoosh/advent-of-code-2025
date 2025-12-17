"""
Python implementation of the solution for day 6 of Advent of Code 2025
"""

import math


def main(input_file_name: str) -> int:
    with open(input_file_name, "r", encoding="utf-8") as input_file:
        input_data_raw: list[str] = input_file.read().splitlines()

    # Transpose the data into columnar lists
    input_columnar: list[list[str]] = list(map(list, zip(*input_data_raw)))

    problems: list[list[str]] = []
    column_buffer: list[str] = []
    # Loop over the columns, right to left
    for line in reversed(input_columnar):
        # Check if the current column is a spaces column, if so output the buffer
        if all(val == " " for val in line):
            problems.append(column_buffer)
            column_buffer = []
            continue

        # Grab the operand if it's there
        operand = line.pop()

        # Merge the digits in the line
        value: str = ""
        for val in line:
            if val != " ":
                value += val

        column_buffer.append(value)
        if operand != " ":
            column_buffer.append(operand)

    # Append the last problem as no space column
    problems.append(column_buffer)

    problem_results: list[int] = []
    for problem in problems:
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
    print(f"Result: {result} ({'Pass' if result == 3263827 else 'Fail'})")
    print("### Main ###")
    print(f"Result: {main('input.txt')}")
